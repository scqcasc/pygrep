import argparse
import sys
from libs import grep, display

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", help="Define file to grep.")
    parser.add_argument(
        "-p",
        "--pattern",
        action="append",
        help="Pattern to search for.  Use multiple --patterns if wanted. You must define at least one pattern.",
    )
    parser.add_argument(
        "--nc",
        action="store_true",
        default=False,
        help="Turn off colour of found pattern.",
    )
    parser.add_argument(
        "--ln", action="store_true", default=False, help="Turn on line numbers."
    )
    parser.add_argument("-w", "--word", action="store_true", default=False, help="Search for whole word only.")
    parser.add_argument("-nf", action="store_true", default=False, help="No fancy colour specification.")

    args = parser.parse_args()
    if args.pattern is None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    results = grep(args.pattern, args.file, args.nc, args.word, args.nf)
    display(results, args.ln)
