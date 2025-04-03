# 🔋♻️ BatteryID: ensemble battery identification model
This tool is intended to pair with a CofC capstone tool to provide battery detection suppport in the application's backend. Given a fed-in image, it can determine the kind of battery, its chemistry, and its recyling instructions.

Because of its ensemble-style design, models trained to find a specific class of battery can be added to increase range and accuracies of decisions.

### Currently, can identify:
1. Li-Ion polymer phone batteries
2. Li-Ion phone batteries

________________

## Installing dependencies
To run this application, pandas (for testing capabilities), OpenOCR, onnx, and Roboflow's inference cli are all required. For proper installation, make sure you are working in a python venv of version **3.11 or earlier**. Inference-cli is not supported in version 3.12 because of a deprecated+removed dependency.
Install dependencies:
```shell
pip install pandas
pip install inference-cli
pip install openocr-python
pip install onnxruntime
```
To learn more about these dependencies, visit:
1. [OpenOCR](https://github.com/Topdu/OpenOCR/tree/main) 
2. [pandas](https://pandas.pydata.org/)
3. [Roboflow Inference CLI](https://inference.roboflow.com/inference_helpers/inference_cli/)
__________________
## Authors and Contributors:
1. Joanna Z. Godawa [(godawajz)](https://github.com/godawajz)
