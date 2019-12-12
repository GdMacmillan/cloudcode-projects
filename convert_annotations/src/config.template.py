import json

config_dict = \
    {
        "project": "",
        "credentials": "GOOGLE_APPLICATION_CREDENTIALS",
        "convert_annotations": {
            "readBucket": "open-images-challenge-data/input",
            "outputFile": "train-annotations-coco.json.",
            "inputFile": "train-annotations-bbox.csv",
            "labelsFile": "class-descriptions-boxable.csv"
        }
    }

if __name__ == "__main__":
    with open('/data/config.json', 'w') as f:
        f.write(json.dumps(config_dict))
