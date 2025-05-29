COLOURS = {}
COLOURS["RED"] = "\033[31m"
COLOURS["GREEN"] = "\033[32m"
COLOURS["RESET"] = "\033[0m"


def grep(pattern: list, file_name: str, nc: bool, word: bool = False) -> list[any]:
    lines = []
    with open(file_name, "r") as f:
        x = 1
        for line in f.readlines():
            line = line.strip()
            for p in pattern:
                if word:
                    p = f' {p} '
                if p in line:
                    if not nc:
                        line = line.replace(
                            p, f"{COLOURS['GREEN']}{p}{COLOURS['RESET']}"
                        )
                    lines.append((x, line))
            x = x + 1
    return lines


def display(results: list, ln: bool) -> None:
    for result in results:
        if not ln:
            print(f"{result[1]}")
        if ln:
            print(f"{result[0]}\t{result[1]}")
