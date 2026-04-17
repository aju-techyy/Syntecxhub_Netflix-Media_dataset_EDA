import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import os

# load dataset
df = pd.read_csv("netflix_titles.csv")

# create output folder for saving plots
os.makedirs("output", exist_ok=True)

# ── basic inspection ──────────────────────────────────────────────────────────

print("shape:", df.shape)
print("\ndtypes:\n", df.dtypes)
print("\nmissing values:\n", df.isnull().sum())
print("\nsample rows:\n", df.head(3))

# ── clean up date and year columns ───────────────────────────────────────────

df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

# drop rows with no type or title
df = df.dropna(subset=["type", "title"])

# ── 1. content count by type (movie vs tv show) ───────────────────────────────

type_counts = df["type"].value_counts()
print("\ncontent type counts:\n", type_counts)

fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(type_counts.index, type_counts.values, color=["#e50914", "#221f1f"], width=0.5)
ax.set_title("content count by type", fontsize=13)
ax.set_xlabel("type")
ax.set_ylabel("count")
for i, v in enumerate(type_counts.values):
    ax.text(i, v + 20, str(v), ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("output/01_content_by_type.png", dpi=150)
plt.close()
print("saved: 01_content_by_type.png")

# ── 2. content added per year (growth over time) ──────────────────────────────

yearly = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)
yearly = yearly[yearly.index >= 2010]  # filter noise from early years

fig, ax = plt.subplots(figsize=(10, 5))
yearly.plot(kind="bar", ax=ax, color=["#e50914", "#b3b3b3"], width=0.7)
ax.set_title("content added to netflix per year", fontsize=13)
ax.set_xlabel("year")
ax.set_ylabel("titles added")
ax.legend(title="type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/02_content_growth_per_year.png", dpi=150)
plt.close()
print("saved: 02_content_growth_per_year.png")

# ── 3. top 10 genres ──────────────────────────────────────────────────────────

# listed_in column has comma-separated genres, split and count each
genres = df["listed_in"].dropna().str.split(",").explode().str.strip()
top_genres = genres.value_counts().head(10)
print("\ntop 10 genres:\n", top_genres)

fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(top_genres.index[::-1], top_genres.values[::-1], color="#e50914")
ax.set_title("top 10 genres on netflix", fontsize=13)
ax.set_xlabel("number of titles")
plt.tight_layout()
plt.savefig("output/03_top10_genres.png", dpi=150)
plt.close()
print("saved: 03_top10_genres.png")

# ── 4. top 10 release years ───────────────────────────────────────────────────

top_years = df["release_year"].value_counts().dropna().head(10).sort_index()
print("\ntop 10 release years:\n", top_years)

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(top_years.index.astype(int).astype(str), top_years.values, color="#221f1f", width=0.6)
ax.set_title("top 10 release years (by number of titles)", fontsize=13)
ax.set_xlabel("release year")
ax.set_ylabel("count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/04_top10_release_years.png", dpi=150)
plt.close()
print("saved: 04_top10_release_years.png")

# ── 5. movie runtime distribution ─────────────────────────────────────────────

movies = df[df["type"] == "Movie"].copy()
movies["duration_min"] = movies["duration"].str.extract(r"(\d+)").astype(float)

fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(movies["duration_min"].dropna(), bins=40, color="#e50914", edgecolor="white")
ax.set_title("movie runtime distribution", fontsize=13)
ax.set_xlabel("duration (minutes)")
ax.set_ylabel("number of movies")
plt.tight_layout()
plt.savefig("output/05_movie_runtime_distribution.png", dpi=150)
plt.close()
print("saved: 05_movie_runtime_distribution.png")

# ── 6. tv show seasons distribution ──────────────────────────────────────────

shows = df[df["type"] == "TV Show"].copy()
shows["seasons"] = shows["duration"].str.extract(r"(\d+)").astype(float)

season_counts = shows["seasons"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(season_counts.index.astype(int).astype(str), season_counts.values, color="#221f1f", width=0.6)
ax.set_title("tv show seasons distribution", fontsize=13)
ax.set_xlabel("number of seasons")
ax.set_ylabel("number of shows")
plt.tight_layout()
plt.savefig("output/06_tvshow_seasons_distribution.png", dpi=150)
plt.close()
print("saved: 06_tvshow_seasons_distribution.png")

# ── 7. top 10 countries producing content ─────────────────────────────────────

countries = df["country"].dropna().str.split(",").explode().str.strip()
top_countries = countries.value_counts().head(10)
print("\ntop 10 countries:\n", top_countries)

fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(top_countries.index[::-1], top_countries.values[::-1], color="#e50914")
ax.set_title("top 10 countries producing netflix content", fontsize=13)
ax.set_xlabel("number of titles")
plt.tight_layout()
plt.savefig("output/07_top10_countries.png", dpi=150)
plt.close()
print("saved: 07_top10_countries.png")

print("\nall plots saved to output/ folder.")