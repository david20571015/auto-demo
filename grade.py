import sys
from argparse import ArgumentParser
from pathlib import Path

from colorama import Fore, init

from src.grader import Grader

init(autoreset=True, wrap=True)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path.cwd()

    return f'{str(base_path)}\\{relative_path}'


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='grade.py',
        description='Run this program to grade your execution files.')
    parser.add_argument('--execution-dir',
                        '-e',
                        default='.\\exec',
                        type=str,
                        help='The directory of execution files.')
    parser.add_argument('--testcase-file',
                        '-t',
                        default='.\\test.json',
                        type=str,
                        help='The file of test cases.')
    args = parser.parse_args()

    grader = Grader(execution_dir=args.execution_dir)
    grader.parse_testcase_file(args.testcase_file)
    grader.judge()

    input("Press any key to continue...")
