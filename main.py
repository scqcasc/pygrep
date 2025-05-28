import argparse
from libs import grep, display

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", help="Define file to grep")
    parser.add_argument(
        "-p",
        "--pattern",
        action="append",
        help="Pattern to search for.  Use multiple --patterns if wanted.",
    )
    parser.add_argument(
        "--nc",
        action="store_true",
        default=False,
        help="Turn off colour of found pattern",
    )
    parser.add_argument(
        "--ln", action="store_true", default=False, help="Turn on line numbers"
    )

    args = parser.parse_args()
    results = grep(args.pattern, args.file, args.nc)
    display(results, args.ln)
