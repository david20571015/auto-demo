from argparse import ArgumentParser

from src.TestLoader import TestLoader

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--test-dir', '-t', default='.\\test', type=str)
    parser.add_argument('--output', '-o', default='.\\test.json', type=str)
    args = parser.parse_args()

    loader = TestLoader(test_dir=args.test_dir)
    loader.gen_json(args.output)
