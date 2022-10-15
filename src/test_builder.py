import json
import os
import subprocess
from pathlib import Path

from colorama import Fore, init

from .env_var import EXECUTION_SUFFIX

init(autoreset=True, wrap=True)


class TestBuilder(object):

    def __init__(self, execution_dir=f'.{os.sep}exec'):
        self.execution_dir = execution_dir
        if not Path(self.execution_dir).is_dir():
            raise FileNotFoundError(f'{self.execution_dir} not found.')

        self.testcases = []

    def parse_test_file(self, test_file=f'.{os.sep}test.in'):
        if not Path(test_file).is_file():
            raise FileNotFoundError(f'{test_file} not found.')

        with open(test_file, 'r') as f:
            while True:
                id, print_detail, *mask_range = f.readline().strip().split(' ')

                mask = []
                for start, end in zip(mask_range[::2], mask_range[1::2]):
                    start = int(start)
                    end = int(end) + 1
                    mask.extend(list(range(start, end)))

                n_cases = int(f.readline())
                inputs = [f.readline().strip() for _ in range(n_cases)]

                testcase = {
                    'id': id,
                    'print_detail': print_detail != '0',
                    'mask': mask,
                    'inputs': inputs
                }
                self.testcases.append(testcase)

                if not f.readline():
                    break

    def execute(self):
        for testcase in self.testcases:
            print(f'Question {testcase["id"]}. ', end='')

            execution_file = f'{self.execution_dir}{os.sep}{testcase["id"]}{EXECUTION_SUFFIX}'
            if not Path(execution_file).is_file():
                print(Fore.RED + 'Error: ' + Fore.RESET +
                      f'{execution_file} not found')
                continue

            outputs = []
            for input in testcase["inputs"]:
                output = subprocess.run(execution_file,
                                        stdout=subprocess.PIPE,
                                        input=input,
                                        encoding='UTF-8').stdout
                outputs.append(output)
            testcase |= {'outputs': outputs}

            print(Fore.GREEN + 'Successed: ' + Fore.RESET +
                  f'got {len(outputs)} test cases.')

    def dump_outputs(self, output_dir=f'.{os.sep}outputs'):
        if 'outputs' not in self.testcases[0].keys():
            raise RuntimeError(
                'Please invoke TestBuilder.execute() before invoke this function.'
            )
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for testcase in self.testcases:
            for i, output in enumerate(testcase["outputs"]):
                with open(f'{output_dir}{os.sep}{testcase["id"]}-{i+1}.txt',
                          'w') as f:
                    print(output, end='', file=f)

        with open(f'{output_dir}{os.sep}all.txt', 'w') as f:
            for testcase in self.testcases:
                for i, output in enumerate(testcase["outputs"]):
                    print(f'# {testcase["id"]}-{i+1}', file=f)
                    print(output, file=f)
                    print('-' * 20, file=f)

    def to_json(self, filename=f'.{os.sep}test.json'):
        with open(filename, 'w') as f:
            json.dump(self.testcases, fp=f, indent=2)
