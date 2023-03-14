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

"""Main file of the project"""

import argparse
import logging

from myapp.module1.service1 import svc1_hello
from myapp.module2.service2 import svc2_hello


def parse_args():
    """Parses command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-e',
                        '--example',
                        action='store_true',
                        help='Print an example message')

    args = parser.parse_args()

    # Check that at least one argument is provided
    if not args.example:
        logging.error('At least one argument is required.')
        parser.error('At least one argument is required.')

    return args


def main():
    """main function

    """

    # Set up logging
    logging.basicConfig(filename='.myproject.log',
                        level=logging.DEBUG,
                        filemode='w')

    logging.info('Executing the main function...')

    args = parse_args()

    if args.example:
        logging.info('Executing the --example argument')
        print('Hello world!')
        svc1_hello()
        svc2_hello()


    logging.info('Exiting...')


if __name__ == '__main__':
    main()
