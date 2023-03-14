# ChartAnalysis

[![Python package](https://github.com/fminna/python_skeleton/actions/workflows/python_test.yaml/badge.svg?branch=master)](https://github.com/fminna/python_skeleton/actions/workflows/python_test.yaml) | [![Docker build and push Image](https://github.com/fminna/python_skeleton/actions/workflows/docker_push.yaml/badge.svg?branch=master)](https://github.com/fminna/python_skeleton/actions/workflows/docker_push.yaml)

A tool to analyze and fix Helm Charts.

----------

## How to Run

First, clone the repository:

```bash
git clone https://github.com/fminna/ChartAnalysis.git
cd ChartAnalysis
```

1. To run in the CLI, use the following commands:

```bash
pipenv shell
pip install .
chartanalysis -h
```

2. To run as a Docker container, use the following commands:

```bash
docker build -t chartanalysis .

docker run chartanalysis -h
```

----------

## Code Style

It is a very good practice to follow a coding style guide. For Python, I recommend the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Following this guide also allows the automatic generation of the Documentation.

----------

## Documentation

The Documentation for this project is automatically generated using the [Sphinx](https://www.sphinx-doc.org/en/master/) tool.

----------
