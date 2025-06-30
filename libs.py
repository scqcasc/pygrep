import sys

COLOURS = {}
COLOURS["RED"] = "\033[31m"
COLOURS["GREEN"] = "\033[32m"
COLOURS['BLUE'] = "\033[34m"
COLOURS['YELLOW'] = "\033[33m"
COLOURS["RESET"] = "\033[0m"

def parse_pattern(pattern: str, nf: bool) -> tuple:
    c = 'GREEN'
    p = pattern
    if not nf:
        if '^^' in pattern:
            (p, c) = pattern.split('^^')

            # if they try an undefined colour default to green
            try:
                COLOURS[c.upper()]
            except KeyError:
                c = 'GREEN'
    return (p, c.upper())

def grep(pattern: list, file_name: str, nc: bool, word: bool = False, nf: bool = False) -> list:
    lines = []
    try:
        with open(file_name, "r") as f:
            x = 1         # x is the line number which gets added to the grepped data
            for line in f.readlines():
                line = line.strip()
                for pat in pattern:
                    (p, c) = parse_pattern(pat, nf)
                    if word:
                        # if word option is used the surround the pattern with white space
                        p = f' {p} '
                    if p in line:
                        if not nc:
                            line = line.replace(
                                p, f"{COLOURS[c]}{p}{COLOURS['RESET']}"
                            )
                        lines.append((x, line))
                x = x + 1
        return lines
    except Exception as e:
        print(f"Error dealing with file {file_name}: {e}")
        sys.exit(1)


def display(results: list, ln: bool) -> None:
    for result in results:
        if not ln:
            print(f"{result[1]}")
        if ln:
            print(f"{result[0]}\t{result[1]}")
