# daily-quote-cli

A tiny command‑line tool that prints a random inspirational quote.

## Features

- No third‑party dependencies – uses only the Python standard library.
- Works on any platform with Python 3.8+.
- Simple one‑file script that you can copy, fork, or `curl`‑pipe.

## Installation

```sh
# Clone the repo
git clone https://github.com/your-username/daily-quote-cli.git
cd daily-quote-cli

# Make the script executable (optional)
chmod +x quote.py
```

Or just download the single file:

```sh
curl -O https://raw.githubusercontent.com/your-username/daily-quote-cli/main/quote.py
chmod +x quote.py
```

## Usage

```sh
./quote.py
```

Example output:

```
"The only limit to our realization of tomorrow is our doubts of today." — Franklin D. Roosevelt
```

## How it works

The script sends a GET request to the public API `https://api.quotable.io/random`, parses the JSON response and prints the *content* and *author* fields.

## License

This project is released into the public domain (Unlicense). Feel free to reuse, modify, or redistribute it without restriction.
