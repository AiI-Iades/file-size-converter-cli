import argparse

def convert_file_size(value, input_unit, output_unit):
    units = {'b': 1, 'kb': 1024, 'mb': 1024**2, 'gb': 1024**3, 'tb': 1024**4}
    return (value * units[input_unit]) / units[output_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('value', type=float)
    parser.add_argument('--input', choices=['b','kb','mb','gb','tb'], required=True)
    parser.add_argument('--output', choices=['b','kb','mb','gb','tb'], required=True)
    args = parser.parse_args()
    result = convert_file_size(args.value, args.input, args.output)
    print(f'{args.value} {args.input} = {result:.2f} {args.output}')