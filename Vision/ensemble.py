from typing import Final
from inference_sdk import InferenceHTTPClient
from idlelib.pyparse import trans
from PIL.ImageOps import contain
from openocr import OpenOCR
import onnxruntime as onnx
from difflib import SequenceMatcher
import results_cleanup as rc
import location_processing as lp
import ast
import json


DEBUG_CONSOLE_OUTPUT : Final[bool] = False

def initialize_engines() -> tuple[InferenceHTTPClient, OpenOCR]:
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="GI8YLPD35TOSADzsK9QH"
    )
    # OpenOCR engine, for text recognition
    onnx_engine = OpenOCR(backend='onnx', device='cpu')

    return CLIENT, onnx_engine


def send_image_battery(battery_client: InferenceHTTPClient, img_path: str, model_id: str) -> str:
    result1 = battery_client.infer(img_path, model_id=model_id)
    print("Image class: ", ((result1['predictions'])[0])['class'])

    return (result1['predictions'])[0]['class']


def send_image_label(onnx_engine : OpenOCR, img_path : str) -> tuple[list[str | float], float] :
    result2_temp, elapse=onnx_engine(img_path)
    results2: list[str | float] = rc.find_battery_info(result2_temp[0])[0] # because we work with only one battery, only use first
    if DEBUG_CONSOLE_OUTPUT:
        for result in results2:
            print(result)
    return results2, elapse


def make_JSON(battery_type: str, label_result: str, confidence: float, locations: list[str], instructions: str) -> json:
    prediction = {
        "battery_class": battery_type,
        "label_result": label_result,
        "confidence": confidence,
        "locations": locations,
        instructions: instructions
    }
    return json.dumps(prediction)


def execute(img_path: str) -> json:
    CLIENT: InferenceHTTPClient # Roboflow client, for battery detection
    onnx_engine: OpenOCR  # OpenOCR engine, for text recognition
    openOCR_results : tuple[list[str | float], float] = ["", 0.0], 0.0

    label_result: list[str | float] = ["", 0.0]
    time: float = 0.0

    inference_results : str = ""

    CLIENT, onnx_engine = initialize_engines()

    img_path = img_path
    model_id = 'iisc/10'

    inference_results = send_image_battery(CLIENT, img_path, model_id)
    openOCR_results = send_image_label(onnx_engine, img_path)

    label_result, time = openOCR_results

    return make_JSON(inference_results, label_result[0], round(label_result[1], 2), lp.get_location_dummy(label_result[0]), lp.get_instructions(label_result[0]))


def main():
    analysis: json = execute('test.jpg')
    print(analysis)


if __name__ == "__main__":
    main()