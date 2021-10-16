import subprocess

from pathlib import Path

class Grader(object):
    def __init__(self, execution: str, question: dict):
        if not Path(execution).is_file():
            raise ValueError(f'Can\'t find {execution}.')

        self.execution = execution
        self.io_pair = zip(question["inputs"], question["outputs"])


    def judge(self):
        total = 0
        correct = 0
        for (input, output) in self.io_pair:
            if self.check(input, output):
                correct += 1
            total += 1
        return correct, total


    def check(self, input: str, output: str): 
        proc = subprocess.run(
            self.execution,
            stdout=subprocess.PIPE,
            input=input,
            encoding='ascii'
        )

        if proc.stderr:
            raise RuntimeError(proc.stderr)

        return proc.stdout == output