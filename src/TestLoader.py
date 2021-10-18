from pathlib import Path
import json
import subprocess


class TestLoader(object):

    def __init__(self, test_dir: str = './test'):
        self.test_dir = Path('.') / test_dir

        self.ids = []
        for child in self.test_dir.iterdir():
            if child.is_dir() and child.name.isdigit():
                self.ids.append(child.name)

    def gen_json(self, filename):
        questions = []
        for id in self.ids:
            io_texts = self.load_io_pair(id)
            ques_dict = {
                "id": id,
                "inputs": io_texts[0],
                "outputs": io_texts[1]
            }
            questions.append(ques_dict)

        with open(filename, 'w') as f:
            json.dump(questions, fp=f, indent=4)

    def load_io_pair(self, id: str):
        io_pair_dir = self.test_dir / id

        if not io_pair_dir.exists():
            raise ValueError(f'Can\'t find {str(io_pair_dir)}.')
        if not io_pair_dir.is_dir():
            raise ValueError(f'{str(io_pair_dir)} should be a directory.')

        input_files = list(io_pair_dir.glob('*.in'))
        output_files = []

        for input_file in input_files:
            output_file = Path(str(input_file).replace('.in', '.out'))

            if not output_file.exists() or not output_file.is_file():
                input_files.remove(input_file)
            else:
                output_files.append(output_file)

        print(f'Found {len(input_files)} test cases for question {id}.')

        input_texts = [i.read_text() for i in input_files]
        output_texts = [o.read_text() for o in output_files]

        return input_texts, output_texts