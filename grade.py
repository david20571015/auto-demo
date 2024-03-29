from argparse import ArgumentParser
import os
from pathlib import Path
import sys

from colorama import init

from auto_demo.grader import Grader

init(autoreset=True, wrap=True)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # pylint: disable=protected-access # type: ignore
    except AttributeError:
        base_path = Path.cwd()

    return f'{str(base_path)}{os.sep}{relative_path}'


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='grade.py',
        description='Run this program to grade your execution files.')
    parser.add_argument('--verification-digit',
                        '--veri-digit',
                        '-v',
                        default=5,
                        type=int,
                        help='''The index that shows the verification digit.
                            The index is starts from 1. For example, 5 means
                            that the 5th and 6th digits are verification
                            codes.''')
    parser.add_argument('--execution-dir',
                        '-e',
                        default='.',
                        type=str,
                        help='The directory of execution files.')
    parser.add_argument('--testcase-file',
                        '-t',
                        default=f'.{os.sep}test.json',
                        type=str,
                        help='The file of test cases.')
    args = parser.parse_args()

    grader = Grader(execution_dir=args.execution_dir)
    grader.print_verification_code(args.verification_digit - 1)
    grader.parse_testcase_file(resource_path(args.testcase_file))
    grader.judge()

    input("Press any key to continue...")
