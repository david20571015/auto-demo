from argparse import ArgumentParser

from src.test_builder import TestBuilder

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='build_test.py',
        description='Run this program to generate test cases JSON file.')
    parser.add_argument('--execution-dir',
                        '-e',
                        default='.\\exec',
                        type=str,
                        help='The directory of execution files.')
    parser.add_argument('--test-file',
                        '-t',
                        default='.\\test.in',
                        type=str,
                        help='The file of input data.')
    parser.add_argument('--output-dir',
                        '-o',
                        type=str,
                        help='The directory of output data.')
    parser.add_argument('--json-file',
                        '-j',
                        default='.\\test.json',
                        type=str,
                        help='The file of test cases.')
    args = parser.parse_args()

    builder = TestBuilder(execution_dir=args.execution_dir)
    builder.parse_test_file(test_file=args.test_file)
    builder.execute()
    builder.to_json(filename=args.json_file)

    if args.output_dir:
        builder.dump_outputs(output_dir=args.output_dir)
