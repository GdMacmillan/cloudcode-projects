import json

config_dict = \
    {
        "project": "",
        "credentials": "GOOGLE_APPLICATION_CREDENTIALS",
        "test_read_annotations": {
            "readBucket": "open-images-challenge-data/input",
            "inputFile": "train-annotations-bbox.csv"
        }
    }

if __name__ == "__main__":
    with open('/data/config.json', 'w') as f:
        f.write(json.dumps(config_dict))
