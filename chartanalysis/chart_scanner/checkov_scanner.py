# Copyright 2023 AssureMOSS
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

"""Running Checkov on a Helm Chart

"""

from typing import List
import logging
import subprocess
import yaml


def parse_yaml_list(file_path: str, list_key: str) -> List[str]:
    """
    Parses a YAML file and returns the value of a specific key as a list.

    Args:
        file_path: A string representing the path to the YAML file to parse.
        list_key: A string representing the key to retrieve the list from.

    Returns:
        A list of strings representing the values of the specified key.

    Raises:
        KeyError: If the specified key is not found in the YAML file.
        FileNotFoundError: If the specified file is not found.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(file_path, 'r') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data[list_key]
    except KeyError as e:
        logging.error('Error while parsing YAML file.')
        raise e
    except FileNotFoundError as e:
        logging.error('Error while parsing YAML file.')
        raise e
    except yaml.YAMLError as e:
        logging.error('Error while parsing YAML file.')
        raise e


def run_checkov(chart_path: str):
    """
    Function to run checkov on a Helm Chart.

    Args:
        chart_path: A string representing the path to a Helm Chart.

    Raises:
        subprocess.CalledProcessError: If the Bash command returns a non-zero exit code.
        OSError: If the Bash command could not be executed.
    """

    logging.info('Running checkov scanner')

    try:
        # Retrieve checkov ignored checks, if any
        ignored_checks = parse_yaml_list(chart_path + '.skip_checks.yaml', 'ignored_checkov_checks')
        ignore = ''
        if ignored_checks:
            ignore = ' --skip-check ' + ','.join(ignored_checks)

        # Run checkov and generate JSON output
        docker_cmd = 'docker run --tty -v ~' + chart_path + ':/chart --workdir /chart bridgecrew/checkov -d . --quiet --compact --framework helm' + ignore + ' -o json --output-file-path scan.json'
        
        subprocess.check_call(docker_cmd, shell=True)
        logging.info('checkov scan result is in scan.json')

    except subprocess.CalledProcessError as e:
        logging.error('Error while runing bash command.')
        raise e
    except OSError as e:
        logging.error('Error while runing bash command.')
        raise e
