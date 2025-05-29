# pygrep
Just a rewrite of grep for S&amp;Gs

## Usage
```
python main.py --help
usage: main.py [-h] [-f FILE] [-p PATTERN] [--nc] [--ln] [-w]

options:
  -h, --help            show this help message and exit
  -f, --file FILE       Define file to grep.
  -p, --pattern PATTERN
                        Pattern to search for. Use multiple --patterns if wanted.
  --nc                  Turn off colour of found pattern.
  --ln                  Turn on line numbers.
  -w, --word            Search for whole word only.
```

## TODO
- [ ] Allow for different colours by pattern
- [ ] Allow for stdin as input
- [ ] Support actual regular expressions (because, you know ... gREp)
