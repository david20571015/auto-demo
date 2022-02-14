import json
import os
import random
import subprocess
from datetime import datetime
from io import StringIO
from pathlib import Path

from colorama import Back, Fore, init

from .env_var import EXECUTION_SUFFIX

init(autoreset=True, wrap=True)


class Grader(object):

    def __init__(self, execution_dir=f'.{os.sep}exec'):
        self.execution_dir = execution_dir
        if not Path(self.execution_dir).is_dir():
            raise FileNotFoundError(f'{self.execution_dir} not found.')

        self.testcases = []

    def print_verification_code(self,
                                index=5,
                                shift=10,
                                block_size=4,
                                n_blocks=3):
        veri_code = (datetime.now().minute + shift) % 100

        veri_seq = ''.join(
            [str(random.randint(0, 9)) for _ in range(block_size * n_blocks)])
        veri_seq = veri_seq[:index] + str(veri_code) + veri_seq[index + 2:]

        veri_block = [
            veri_seq[i:i + block_size]
            for i in range(0, len(veri_seq), block_size)
        ]

        print('-'.join(veri_block))

    def judge(self):
        if not self.testcases:
            raise RuntimeError(
                'Please invoke Grader.parse_testcase_file() before invoke this function.'
            )

        for testcase in self.testcases:
            print(f'{testcase["id"]}. ', end='')

            execution_file = f'{self.execution_dir}{os.sep}{testcase["id"]}{EXECUTION_SUFFIX}'
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

            mask = testcase['mask'] if testcase['print_detail'] else []
            self._print_result(correct, len(testcase['inputs']), log, mask)

    def parse_testcase_file(self, testcase_file=f'.{os.sep}test.json'):
        if not Path(testcase_file).is_file():
            raise FileNotFoundError(f'{testcase_file} not found.')

        with open(testcase_file, 'r') as f:
            self.testcases = json.load(f)

    def _print_result(self,
                      correct,
                      total,
                      log: list[tuple[str, str]],
                      mask=[]):
        if total == 0:
            print(Fore.RED + 'ERROR: ' + Fore.RESET +
                  'There is no test data for this question.')
        elif correct == total:
            print(Fore.GREEN + 'PASS: ' + Fore.RESET + f'{correct} / {total}')
        else:
            print(Fore.RED + 'FAIL: ' + Fore.RESET + f'{correct} / {total}')
            for student_output, output in log:
                self._print_details(student_output, output, mask)

    def _print_details(self, output, answer, mask=[]):

        def parse_text(text):
            return [
                [str(len(line)), line] for line in StringIO(text).readlines()
            ]

        def print_line(lines, mask=[]):
            for i, (length, line) in enumerate(lines):
                info = f'{i+1:>2}. {length:<3}'
                if i + 1 in mask:
                    result = Fore.LIGHTBLACK_EX + '(hidden)' + Fore.RESET
                else:
                    result = line.replace('\n',
                                          Back.MAGENTA + '\\n' + Back.RESET)
                print(' ' * 8 + f'{info}|{result}')

        output_lines = parse_text(output)
        answer_lines = parse_text(answer)

        # Redundant output lines are all wrong.
        for i in range(len(answer_lines), len(output_lines)):
            output_lines[i][1] = Back.RED + output_lines[i][1] + Back.RESET

        for i in range(min(len(answer_lines), len(output_lines))):
            if output_lines[i][1] == answer_lines[i][1]:
                continue

            # Mark wrong line length.
            if output_lines[i][0] != answer_lines[i][0]:
                output_lines[i][0] = Back.RED + output_lines[i][0] + Back.RESET + \
                    ' ' * (3 - len(output_lines[i][0])) # Pad spece to fit the output format.

                if output_lines[i][0] > answer_lines[i][0]:
                    first_redundant_pos = int(answer_lines[i][0])
                    output_lines[i][1] = \
                        output_lines[i][1][:first_redundant_pos] + \
                        Back.RED + output_lines[i][1][first_redundant_pos:]

            # Mark from first wrong character.
            for j in range(min(len(answer_lines[i][1]),
                               len(output_lines[i][1]))):
                if output_lines[i][1][j] != answer_lines[i][1][j]:
                    output_lines[i][1] = \
                        output_lines[i][1][:j] + Back.RED + output_lines[i][1][j:]
                    break

        print(' ' * 8 + Fore.LIGHTRED_EX + '#' * 20 + ' YOUR OUTPUT ' +
              '#' * 21)
        print_line(output_lines)
        print(' ' * 8 + Fore.LIGHTGREEN_EX + '-' * 23 + ' ANSWER ' + '-' * 23)
        print_line(answer_lines, mask)
        print(' ' * 8 + Fore.LIGHTCYAN_EX + '#' * 54)

    def _execute(self, execution: str, input: str) -> str:
        proc = subprocess.run(execution,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              input=input,
                              encoding='ascii')
        return proc.stdout or proc.stderr
