# 🎬 Top 50 Films Data Pipeline

## 📌 Project Overview

This project is a simple **data pipeline** that scrapes movie data from a web source, processes it using Python, and stores it in both a CSV file and a SQLite database.

It demonstrates core data engineering concepts:

* Web scraping
* Data transformation
* Data storage (CSV + database)

---

## ⚙️ Tech Stack

* Python 🐍
* Requests (HTTP requests)
* BeautifulSoup (web scraping)
* Pandas (data manipulation)
* SQLite3 (database)

---

## 🔄 Workflow

### 1. Web Scraping

* Data is extracted from:

  * Archived webpage: *Top 100 Highly Ranked Films*
* The script extracts:

  * Average Rank
  * Film Name
  * Year

---

### 2. Data Processing

* Cleans and structures the extracted data
* Stores the results in a Pandas DataFrame

---

### 3. Data Storage

The processed data is saved in two formats:

#### 📄 CSV File

* Stored locally as a structured file for easy access and sharing

#### 🗄️ SQLite Database

* Data is stored in a table named `Top_50`
* Enables SQL-based querying and analysis

---

## 📂 Project Structure

```id="x8v7w2"
.
├── script.py
├── top_50_films.csv
├── Movies.db
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash id="b3k9l1"
pip install requests pandas beautifulsoup4
```

### 2. Run the script

```bash id="c7k2d4"
python script.py
```

---

## 📊 Output

* A clean dataset of top-ranked films
* CSV file for external use
* SQLite database for querying
* Printed preview of the dataset

---

## 🧠 Key Concepts Demonstrated

* Web scraping with BeautifulSoup
* Data cleaning and structuring with Pandas
* Saving data to CSV
* Storing data in a relational database (SQLite)
* Handling and validating scraped data

---

## ⚠️ Notes

* The data source is from an archived webpage, so structure may change over time.
* Ensure stable internet connection when running the script.
* File paths may need adjustment depending on your system.

---

## ✨ Author

Built as part of a data engineering learning journey — focused on building practical ETL pipelines and working with real-world data sources.

