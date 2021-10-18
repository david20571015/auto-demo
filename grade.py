from argparse import ArgumentParser
import json
from pathlib import Path
import sys

from colorama import init, Fore

from src.Grader import Grader

init(autoreset=True, wrap=True)


def print_result(correct, total):
    if correct == total:
        print(Fore.GREEN + f'{"PASS":<6}', end='')
    else:
        print(Fore.RED + f'{"FAIL":<6}', end='')

    print(f'{correct} / {total}')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path.cwd()

    return f'{str(base_path)}\\{relative_path}'


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--test-file', '-t', default='.\\test.json', type=str)
    parser.add_argument('--execution-dir', '-e', default='.', type=str)
    args = parser.parse_args()

    with open(resource_path(args.test_file), 'r') as fp:
        questions = json.load(fp)

    for q in questions:
        execution_file = f'{args.execution_dir}\\{q["id"]}.exe'

        try:
            print(f'{q["id"] + ".":<3}', end='')
            grader = Grader(execution_file, q)
            correct, total = grader.judge()
            print_result(correct, total)

        except Exception as err:
            print(Fore.RED + f'{"ERROR":<6}', end='')
            print(err)

    input("Press any key to continue...")
