import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff between two files.")
    parser.add_argument("first_file", help="path to the first file")
    parser.add_argument("second_file", help="path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help="set format of output (default: stylish)",
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
