# Copyright 2023 MyOrganization
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Setup script for my project.

"""

import subprocess
from setuptools import setup, find_packages
from pkg_resources import parse_requirements


# Run Sphinx make html command
try:
    subprocess.check_call('cd ./docs && make clean && make html && sphinx-build -b html -d _build/doctrees . html', shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


# Parse requirements.txt file
with open('requirements.txt') as f:
    reqs = [str(req) for req in parse_requirements(f) if not str(req).startswith('-i')]


setup(
    name="my-python-project",
    version="1.0",
    author="Francesco Minna", 
    description="Lorem Ipsum",
    packages=find_packages(),
    package_dir={'myapp': 'myapp'},
    entry_points={
        'console_scripts': [
            'myapp=myapp.__main__:main'
        ],
    },
    install_requires=reqs,
)
