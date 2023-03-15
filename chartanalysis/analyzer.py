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

"""Main file of the project"""

import argparse
import logging

from chartanalysis.chart_scanner.checkov_scanner import run_checkov
from chartanalysis.checkov_parser.scan_parser import json_parser


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-rc',
                        '--run-checkov',
                        dest='run_checkov',
                        nargs=1,
                        metavar='helm/chart/path',
                        help='Run checkov on a Helm Chart')

    parser.add_argument('-cp',
                        '--checkov-parser',
                        dest='checkov_parser',
                        nargs=1,
                        metavar='path/to/json',
                        help='Parse checkov JSON output from Helm Chart')

    args = parser.parse_args()

    # Check that at least one argument is provided
    if not (args.run_checkov or args.checkov_parser):
        logging.error('At least one argument is required.')
        parser.error('At least one argument is required.')

    return args


def main():
    """
    main function

    """

    # Set up logging
    logging.basicConfig(filename='.chartanalysis.log',
                        level=logging.DEBUG,
                        filemode='w')

    logging.info('Executing the main function...')

    # Parsing user arguments
    args = parse_args()

    if args.run_checkov:
        logging.info('Executing the --run-checkov argument')
        run_checkov(args.run_checkov[0])

    elif args.checkov_parser:
        logging.info('Executing the --checkov-parser argument')
        json_parser(args.checkov_parser[0])

    # run_cavisor

    # create_seccomp

    # create_apparmor


    logging.info('Exiting...')


if __name__ == '__main__':
    main()
