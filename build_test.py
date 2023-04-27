from argparse import ArgumentParser
import os

from auto_demo.test_builder import TestBuilder

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='build_test.py',
        description='Run this program to generate test cases JSON file.')
    parser.add_argument('--execution-dir',
                        '-e',
                        default=f'.{os.sep}exec',
                        type=str,
                        help='The directory of execution files.')
    parser.add_argument('--test-file',
                        '-t',
                        default=f'.{os.sep}test.in',
                        type=str,
                        help='The file of input data.')
    parser.add_argument('--output-dir',
                        '-o',
                        type=str,
                        help='The directory of output data.')
    parser.add_argument('--json-file',
                        '-j',
                        default=f'.{os.sep}test.json',
                        type=str,
                        help='The file of test cases.')
    args = parser.parse_args()

    builder = TestBuilder(execution_dir=args.execution_dir)
    builder.parse_test_file(test_file=args.test_file)
    builder.execute()
    builder.to_json(filename=args.json_file)

    if args.output_dir:
        builder.dump_outputs(output_dir=args.output_dir)
