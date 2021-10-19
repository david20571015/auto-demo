import json
import subprocess
from pathlib import Path

from colorama import Fore, init

init(autoreset=True, wrap=True)


class Grader(object):

    def __init__(self, execution_dir='.\\exec'):
        self.execution_dir = execution_dir
        if not Path(self.execution_dir).is_dir():
            raise FileNotFoundError(f'{self.execution_dir} not found.')

        self.testcases = []

    def judge(self):
        if not self.testcases:
            raise RuntimeError(
                'Please invoke Grader.parse_testcase_file() before invoke this function.'
            )

        for testcase in self.testcases:
            print(f'{testcase["id"]}. ', end='')

            execution_file = f'{self.execution_dir}\\{testcase["id"]}.exe'
            if not Path(execution_file).is_file():
                print(Fore.RED + 'ERROR: ' + Fore.RESET +
                      f'{execution_file} not found.')
                continue

            correct = 0
            log = []
            for input, output in zip(testcase['inputs'], testcase['outputs']):
                student_output = self._execute(execution_file, input)
                if student_output == output:
                    correct += 1
                elif testcase['print_detail']:
                    log.append((student_output, output))

            self._print_result(correct, len(testcase['inputs']), log)

    def parse_testcase_file(self, testcase_file='.\\test.json'):
        if not Path(testcase_file).is_file():
            raise FileNotFoundError(f'{testcase_file} not found.')

        with open(testcase_file, 'r') as f:
            self.testcases = json.load(f)

    def _print_result(self, correct, total, log: list[tuple[str, str]]):
        if total == 0:
            print(Fore.RED + 'ERROR: ' + Fore.RESET +
                  'There is no test data for this question.')
        elif correct == total:
            print(Fore.GREEN + 'PASS: ' + Fore.RESET + f'{correct} / {total}')
        else:
            print(Fore.RED + 'FAIL: ' + Fore.RESET + f'{correct} / {total}')
            for student_output, output in log:
                print(Fore.LIGHTRED_EX +
                      '############# YOUR OUTPUT #############')
                print(student_output)
                print(Fore.LIGHTGREEN_EX +
                      '+++++++++++++++ ANSWER ++++++++++++++++')
                print(output)
                print(Fore.LIGHTCYAN_EX +
                      '#######################################')

    def _execute(self, execution: str, input: str) -> str:
        proc = subprocess.run(execution,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              input=input,
                              encoding='ascii')
        return proc.stdout or proc.stderr
