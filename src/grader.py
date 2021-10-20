import json
import subprocess
from io import StringIO
from pathlib import Path

from colorama import Back, Fore, init

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
                self._print_details(student_output, output)

    def _print_details(self, student_output, output, mask=[]):

        def print_line(text, mask=[]):
            for i, line in enumerate(StringIO(text).readlines()):
                info = f'{i+1:>2}. {len(line):<3}'
                if i + 1 in mask:
                    result = Fore.LIGHTBLACK_EX + '(hidden)' + Fore.RESET
                else:
                    result = line.replace('\n',
                                          Back.MAGENTA + '\\n' + Back.RESET)
                print(f'{info}|{result}')

        print(Fore.LIGHTRED_EX + '#' * 20 + ' YOUR OUTPUT ' + '#' * 20)
        print_line(student_output)
        print(Fore.LIGHTGREEN_EX + '+' * 23 + ' ANSWER ' + '+' * 23)
        print_line(output, mask)
        print(Fore.LIGHTCYAN_EX + '#' * 54)

    def _execute(self, execution: str, input: str) -> str:
        proc = subprocess.run(execution,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              input=input,
                              encoding='ascii')
        return proc.stdout or proc.stderr
