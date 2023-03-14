# PythonSkeleton

[![Python package](https://github.com/fminna/python_skeleton/actions/workflows/python_test.yaml/badge.svg?branch=master)](https://github.com/fminna/python_skeleton/actions/workflows/python_test.yaml) | [![Docker build and push Image](https://github.com/fminna/python_skeleton/actions/workflows/docker_push.yaml/badge.svg?branch=master)](https://github.com/fminna/python_skeleton/actions/workflows/docker_push.yaml)

A skeleton to create Python applications from scratch.

----------

## How to Run

First, clone the repository:

```bash
git clone https://github.com/fminna/python_skeleton.git
cd python_scheleton
```

1. To run in the CLI, use the following commands:

```bash
pipenv shell
pip install .
myapp -h
```

2. To run as a Docker container, use the following commands:

```bash
docker build -t my-python-project .

docker run my-python-project -h
```

3. To run as a Kubernetes deployment, use the following commands:

```bash
# First, push the Docker image to DockerHub
docker login
docker tag my-python-project:latest <dockerhub-username>/my-python-project:latest
docker push <dockerhub-username>/my-python-project

# Finally, run the Deployment on the K8s cluster
# Remember to change the YAML file specifying your <dockerhub-username>
kubectl apply -f my-python-project.yaml
```

----------

## Code Style

It is a very good practice to follow a coding style guide. For Python, I recommend the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Following this guide also allows the automatic generation of the Documentation.

----------

## Documentation

The Documentation for this project is automatically generated using the [Sphinx](https://www.sphinx-doc.org/en/master/) tool.

----------
