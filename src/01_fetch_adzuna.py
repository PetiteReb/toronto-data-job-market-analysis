"""
01_fetch_adzuna.py
------------------
First fetch from the Adzuna API: retrieves 10 'data analyst' job postings
in Ontario, Canada, and prints a summary to the terminal.

This is a test script to validate API connectivity and credentials.
"""

import os
import requests
from dotenv import load_dotenv

# Load credentials from .env file at the project root
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Sanity check: did we read the credentials properly?
if not APP_ID or not APP_KEY:
    raise RuntimeError(
        "Missing credentials. Make sure ADZUNA_APP_ID and ADZUNA_APP_KEY "
        "are set in your .env file at the project root."
    )


def fetch_jobs(query: str, location: str, results_per_page: int = 10) -> dict:
    """Call the Adzuna search endpoint for Canada and return the JSON response."""
    url = "https://api.adzuna.com/v1/api/jobs/ca/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "where": location,
        "results_per_page": results_per_page,
        "content-type": "application/json",
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()  # Raises an exception on HTTP error (401, 500, etc.)
    return response.json()


def main() -> None:
    print("Fetching 'data analyst' jobs in Ontario...\n")
    data = fetch_jobs(query="data analyst", location="Ontario", results_per_page=10)

    total_found = data.get("count", 0)
    results = data.get("results", [])

    print(f"Total jobs matching this search on Adzuna: {total_found:,}")
    print(f"Returned in this page: {len(results)}\n")
    print("-" * 70)

    for i, job in enumerate(results, start=1):
        title = job.get("title", "N/A")
        company = job.get("company", {}).get("display_name", "N/A")
        location_name = job.get("location", {}).get("display_name", "N/A")
        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")

        if salary_min and salary_max:
            salary = f"${salary_min:,.0f} - ${salary_max:,.0f}"
        else:
            salary = "Not disclosed"

        print(f"{i}. {title}")
        print(f"   Company:  {company}")
        print(f"   Location: {location_name}")
        print(f"   Salary:   {salary}")
        print()


if __name__ == "__main__":
    main()