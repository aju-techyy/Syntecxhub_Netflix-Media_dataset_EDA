# Netflix / Media Dataset EDA

A data science project built during my internship at Syntecxhub.
This project performs exploratory data analysis on the Netflix titles dataset,
covering content distribution, genre trends, runtime analysis, and country-wise production insights.

## Project Structure

Netflix - Media dataset EDA/
├── netflix_eda.py
├── netflix_titles.csv
├── requirements.txt
├── README.md
└── output/
├── 01_content_by_type.png
├── 02_content_growth_per_year.png
├── 03_top10_genres.png
├── 04_top10_release_years.png
├── 05_movie_runtime_distribution.png
├── 06_tvshow_seasons_distribution.png
└── 07_top10_countries.png

## What This Project Does

- Loads and inspects the Netflix titles dataset (missingness, dtypes, shape)
- Analyzes content distribution by type (Movie vs TV Show)
- Tracks content growth added to Netflix per year (from 2010 onward)
- Identifies top 10 genres, release years, and producing countries
- Visualizes movie runtime distribution and TV show season counts
- Exports all 7 plots to an output/ folder

## Libraries Used

- pandas
- matplotlib
- seaborn

## Dataset

Netflix Shows dataset from Kaggle:
https://www.kaggle.com/datasets/shivamb/netflix-shows

