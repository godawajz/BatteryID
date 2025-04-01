from inference_sdk import InferenceHTTPClient
from idlelib.pyparse import trans
from PIL.ImageOps import contain
from openocr import OpenOCR
import onnxruntime as onnx
from difflib import SequenceMatcher
import results_cleanup as rc
import ast


def initialize_engines(battery_client: InferenceHTTPClient, onnx_engine: OpenOCR):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="GI8YLPD35TOSADzsK9QH"
    )
    # OpenOCR engine, for text recognition
    onnx_engine = OpenOCR(backend='onnx', device='cpu')

    return battery_client, onnx_engine


def send_image_battery(battery_client: InferenceHTTPClient, img_path: str, model_id: str):
    result1 = battery_client.infer(img_path, model_id=model_id)
    print("Image class: ", ((result1['predictions'])[0])['class'])
    return result1


def send_image_label(onnx_engine : OpenOCR, img_path : str) :
    result2_temp, elapse=onnx_engine(img_path)
    results2 = find_battery_info(result2_temp[0])
    for result in results2:
        print("Label result: ", result)
    return results2, elapse


def main():
    CLIENT : InferenceHTTPClient # Roboflow client, for battery detection
    onnx_engine : OpenOCR # OpenOCR engine, for text recognition

    CLIENT, onnx_engine = initialize_engines(CLIENT, onnx_engine)

    img_path = 'test.jpg'
    model_id = 'iisc/10'

    send_image_battery(CLIENT, img_path, model_id)
    send_image_label(onnx_engine, img_path)


if __name__ == "__main__":
    main()