# Toronto Data Job Market Analysis

Analysis of 1,000+ data-related job postings in Ontario, Canada, to map the skills landscape, salary trends, and top recruiters in the local data market.

## Project Goal

As a Canadian data consultant relocating from Europe to Ontario, I built this project to:
- Map the skills most demanded by Ontario data employers
- Identify salary benchmarks across roles (Data Analyst, Engineer, Scientist, Consultant, BI)
- Pinpoint top recruiting companies and emerging hubs beyond Toronto

##  Dataset

- **Source**: [Adzuna API](https://developer.adzuna.com/) — Canadian job aggregator
- **Volume**: 1,136 unique job postings collected in May 2026
- **Coverage**: 6 search terms × Ontario (Data Analyst, Data Consultant, BI Analyst, Data Scientist, Business Analyst, Data Engineer)

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