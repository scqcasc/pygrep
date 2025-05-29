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

## Examples

Searching two patterns with whole word selected and line numbers on:
```
$  python main.py -f LICENSE -p IS --pattern ARE --ln -w
15	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
```

Searching two patterns without whole word selected and line numbers on:
```
$  python main.py -f LICENSE -p IS --pattern ARE --ln
15	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
15	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
19	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
```

Same without line numbers
```
$  python main.py -f LICENSE -p IS --pattern ARE
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## TODO
- [ ] Allow for different colours by pattern
- [ ] Allow for stdin as input
- [ ] Support actual regular expressions (because, you know ... gREp)
