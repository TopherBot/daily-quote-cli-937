#!/usr/bin/env python3
"""daily-quote-cli: print a random inspirational quote.

Fetches a random quote from https://api.quotable.io/random and prints it to stdout.
"""

import json
import sys
import urllib.request
from urllib.error import URLError, HTTPError

API_URL = "https://api.quotable.io/random"


def fetch_quote() -> str:
    """Retrieve a quote from the public API and format it.

    Returns:
        A string containing the quote and its author.
    """
    try:
        with urllib.request.urlopen(API_URL, timeout=10) as response:
            if response.status != 200:
                raise RuntimeError(f"Unexpected HTTP status: {response.status}")
            data = json.load(response)
            return f"\"{data.get('content', '')}\" — {data.get('author', '')}"
    except (URLError, HTTPError) as e:
        raise RuntimeError(f"Failed to retrieve quote: {e}") from e


def main(argv=None) -> int:
    """Entry point for the CLI.

    Returns:
        Exit code (0 on success, 1 on error).
    """
    try:
        quote = fetch_quote()
        print(quote)
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
