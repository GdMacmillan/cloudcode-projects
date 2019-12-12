# Python image to use.
FROM python:3.7

WORKDIR /workspace/job
COPY . /workspace/job/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run docker_entrypoint.sh when the container launches
ENTRYPOINT ["/workspace/job/docker_entrypoint.sh"]