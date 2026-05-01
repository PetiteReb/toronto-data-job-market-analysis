"""
Collect data-related job postings from Adzuna and save them as JSON files in the data/ directory.
"""


import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

#---------------------------------------------
#CONFIGURATION
#----------------------------------------------
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

if not APP_ID or not APP_KEY:
    raise RuntimeError("Missing Adzuna credentials. Make sure ADZUNA_APP_ID and ADZUNA_APP_KEY "
        "are set in your .env file at the project root")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

JOB_TITLES = [
    "data analyst",
    "data consultant",
    "BI analyst",
    "data scientist",  
    "business analyst",
    "data engineer"
]

LOCATION = "Ontario"
RESULTS_PER_PAGE = 50
MAX_PAGES_PER_TITLE = 5
DELAY_BETWEEN_REQUESTS_SEC = 1.0  


#---------------------------------------------
#API CALLS
#----------------------------------------------
def fetch_jobs(query, location, page):
    """Fetch a page of job results from Adzuna API."""
    url = f"https://api.adzuna.com/v1/api/jobs/ca/search/{page}"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "where": location,
        "results_per_page": RESULTS_PER_PAGE,
        "content-type": "application/json",
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def collect_all_jobs():
    """Loop over all job titles and pages, return a deduplicated list of jobs."""
    all_jobs = {}    # dict keyed by job ID for automatic dedup

    for title in JOB_TITLES:    # boucle sur les métiers : utilise la constante définie en haut
        print(f"\n=== Searching: '{title}' in {LOCATION} ===")

        for page in range(1, MAX_PAGES_PER_TITLE + 1):    # boucle sur les pages : utilise la constante MAX_PAGES_PER_TITLE
            try:
                data = fetch_jobs(title, LOCATION, page)
            except requests.HTTPError as e:
                print(f"  Page {page}: HTTP error → {e}. Stopping this title.")
                break

            results = data.get("results", [])
            total_count = data.get("count", 0)

            if not results:
                print(f"  Page {page}: no more results.")
                break

            # Compter les nouveaux jobs (pas déjà vus)
            new_jobs = 0
            for job in results:
                job_id = job.get("id")
                if job_id and job_id not in all_jobs:
                    job["_search_query"] = title    # on garde une trace de quelle recherche a trouvé ce job
                    all_jobs[job_id] = job
                    new_jobs += 1

            print(
                f"  Page {page}: got {len(results)} results "
                f"(+{new_jobs} new) — total in API: {total_count:,}"
            )

            # Si la page est incomplète, c'est la dernière
            if len(results) < RESULTS_PER_PAGE:    # compare au nombre attendu de résultats par page
                break

            time.sleep(DELAY_BETWEEN_REQUESTS_SEC)    # respecte le délai défini en haut

    return list(all_jobs.values())
# ---------------------------------------------
# MAIN
# ---------------------------------------------

if __name__ == "__main__":
    print(f"Starting Adzuna data collection for: {', '.join(JOB_TITLES)}")
    print(f"Location filter: {LOCATION}\n")

    jobs = collect_all_jobs()

    # Save to JSON file
    output_file = RAW_DATA_DIR / "adzuna_jobs.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)


    print(f"\n{'=' * 70}")
    print(f"✅ Collection complete! Total unique jobs: {len(jobs)}")
    print(f"{'=' * 70}")

