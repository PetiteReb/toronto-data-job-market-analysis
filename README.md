![Skills Wordcloud](assets/skills_wordcloud.png)

# Mapping the Ontario Data Job Market

This project analyzes 1,369 data job postings across Ontario. Data was collected from two sources: Adzuna's API and Job Bank Open Data (Government of Canada).

## What I Built

This project was built in three steps. First, I queried Adzuna's API using six job title keywords: Data Analyst, Data Engineer, Data Scientist, Data Consultant, Business Analyst, and BI Analyst. Second, on Job Bank, I downloaded three months of data (Feb–April 2026, 147,538 rows) and filtered to Ontario postings under four data-related NOC 2021 codes. Both filters were built on the same hypothesis: that these job titles and NOC codes are most representative of the Ontario data job market.

Before analysis, I standardized salaries (hourly, monthly, or yearly), corrected mislabeled units, and removed outliers to run a cross-source comparison on skills, region, and salary.

## Three Findings That Changed My Job Search Strategy

### Finding 1: Job Bank is two markets in one

When I started exploring Job Bank's salary data, I expected to find a uniform distribution, or one skewed toward the lower end of the salary range. Instead, I found something more interesting. Three of the four NOC codes (representing around 41.5% of the dataset) have a near-zero interquartile range (IQR), clustered around a single salary value:

- 68.8% of Data Scientist postings list a salary of $103,730
- 77.7% of Business Systems Specialist postings list a salary of $96,897
- 62.5% of Database Analyst postings list salaries between $85,280 and $89,471 (a slightly less concentrated pattern)

This is rare in an open labor market, and likely means these are standardized rates set by a federal pay grid covering hundreds of postings. Only the Information Systems Specialists (NOC 21222, representing 58.5% of the dataset) show a genuine market distribution (IQR = $41,465).

For any job seeker scanning Job Bank salary data, this is critical: Job Bank is a combination of two distinct job markets — one driven by a government pay scale, the other operating as an open market.

![Salary distribution by role across Adzuna and Job Bank](assets/salary_by_role_boxplot.png)


## Tech Stack

- **Language**: Python 3.14
- **Data collection**: `requests`, `python-dotenv`
- **Data processing**: `pandas` *(in progress)*
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud` *(in progress)*
- **NLP**: regex-based skill extraction *(in progress)*

## Project Structure

```
toronto-data-job-market-analysis/
├── data/
│   ├── raw/                       # Raw API responses (JSON)
│   └── processed/                 # Cleaned datasets (CSV)
├── src/
│   ├── 01_fetch_adzuna.py         # API connectivity test
│   └── 02_collect_adzuna_jobs.py  # Main data collection pipeline
├── notebooks/                     # Jupyter notebooks for analysis
├── outputs/                       # Charts, reports, exports
├── requirements.txt
└── .env.example                   # Template for API credentials
```

## How to Reproduce

1. Clone this repo:
```bash
   git clone https://github.com/PetiteReb/toronto-data-job-market-analysis.git
   cd toronto-data-job-market-analysis
```

2. Set up Python environment:
```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # Windows
   pip install -r requirements.txt
```

3. Get free Adzuna API credentials at https://developer.adzuna.com/signup, then:
```bash
   cp .env.example .env
   # Edit .env with your ADZUNA_APP_ID and ADZUNA_APP_KEY
```

4. Run the collection script:
```bash
   python src/02_collect_adzuna_jobs.py
```

## Key Findings *(coming soon)*

This section will be updated as the analysis progresses.

## About ME

Rebecca Olivier — Data & Analytics Consultant
Currently in Toulouse, France 
[LinkedIn](https://linkedin.com/in/rebeccaolivier-/) · rebecca.olivier28@gmail.com