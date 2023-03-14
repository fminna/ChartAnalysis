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

# Set the base image to use for the container
FROM python:3-slim-buster

# Set the working directory in the container
WORKDIR /project

# Copy the project code to the container
COPY . .

# Install the dependencies
RUN pip install .

# Set the command to run when the container starts
ENTRYPOINT [ "myapp" ] 