# huntAPI

huntAPI is a small CLI tool for discovering working API endpoints on a target base URL by combining wordlists with HTTP method checks. It can scan for endpoints that respond with `200 OK` and records the accepted HTTP methods for each successful endpoint.

## What It Does

- Prompts for a target base URL (must include `http://` or `https://`).
- Loads a wordlist (default or custom).
- Tries each word as an endpoint and tests `GET`, `POST`, `PATCH`, `PUT`, and `DELETE`.
- Prints results to the console and writes successes to `results/<domain>.csv`.

## Project Layout

- `hunter_api.py`: Bash menu launcher for the two modes.
- `hunting/`: Wordlist-driven endpoint hunting (primary functionality).
- `crawling/`: Placeholder for crawler-based discovery (currently only prompts for URL).
- `default_wordlist/`: Built-in wordlists.
- `custom_wordlist/`: Your custom wordlists (add `.txt` files here).
- `results/`: Output CSV files.

## Requirements

- Python 3.8+
- `pip` dependencies:
  - `requests`
  - `colorama`

## Setup

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install requests colorama
```

## Usage

Run the launcher (recommended):

```bash
./hunter_api.py
```

Then choose:

- `1` for the crawler mode (currently a stub that only prompts for URL).
- `2` for wordlist hunting (main functionality).

### Wordlist Hunting Flow

1. Enter the target base URL (must include `http://` or `https://`).
2. Choose default or custom wordlist.
3. Pick a wordlist file from the list.
4. View results in the console and in `results/<domain>.csv`.

### Custom Wordlists

Add a `.txt` file to `custom_wordlist/` and select it when prompted.

## Output

Successful endpoints are saved as a CSV in `results/` with columns:

- `URL`
- `Response`
- `End-Point`
- `Accepted-Requests`

## Notes

- The scanner treats only `200 OK` as success.
- If a request fails due to connection issues, the run stops with an error message.

## Troubleshooting

- If you see `ModuleNotFoundError`, re-check your `pip install` step.
- If your URL is rejected, ensure it includes `http://` or `https://`.
