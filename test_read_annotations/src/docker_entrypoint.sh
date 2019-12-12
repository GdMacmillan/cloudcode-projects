#!/bin/bash

mkdir /data
cd /data

git config --global user.email "user@email.com"
git config --global user.name "name"
git clone https://github.com/GdMacmillan/kaggle_oic_object_detection.git

cd kaggle_oic_object_detection
git checkout $BRANCH


cd /workspace/job
python config.py
PYTHONPATH=/data/kaggle_oic_object_detection python -m computer_vision.test_read_annotations

sleep 600