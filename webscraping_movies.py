import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# ----------------------------
# CONFIG
# ----------------------------
db_name = 'Movies.db'# Name of the SQLite database file
table_name = 'Top_50'#` Name of the table to store the data in the SQLite database`
csv_path = r'C:\Data Engineering\WEBSCRAPING\top_50_films.csv'# Path to save the CSV file containing the scraped data

df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])#

# ----------------------------
# STEP 1: WEB SCRAPING
# ----------------------------
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'# URL of the webpage to scrape, which contains the list of top 50 films

response = requests.get(url)# Send a GET request to the specified URL and store the response in the variable 'response'
soup = BeautifulSoup(response.text, 'html.parser')# Parse the HTML content of the response using BeautifulSoup and create a soup object for easy navigation and data extraction

tables = soup.find_all('tbody')# Find all <tbody> elements, which contain the table rows

if tables:# Check if any tables were found
    rows = tables[0].find_all('tr')# Find all <tr> elements in the first table, which represent the rows of the table. We assume the first table contains the desired data.

    for row in rows:# Loop through each row in the first table
        cols = row.find_all('td')# Find all <td> elements in the row, which contain the data cells for rank, film, year 

        if len(cols) >= 3:  # Ensure there are at least 3 columns (rank, film, year)
            rank = cols[0].text.strip()# Extract and clean the rank from the first column
            film = cols[1].text.strip()# Extract and clean the film name from the second column
            year = cols[2].text.strip()# Extract and clean the year from the third column

            df.loc[len(df)] = [rank, film, year]# Append the extracted data as a new row in the DataFrame

else:
    print("No table found on page.")

# ----------------------------
# PREVIEW
# ----------------------------
print(df.head())# Print the first few rows of the DataFrame to verify the scraped data

# ----------------------------
# STEP 2: SAVE TO CSV
# ----------------------------
df.to_csv(csv_path, index=False)# Save the DataFrame to a CSV file without the index column
print(f"✅ Data saved to CSV at {csv_path}")

# ----------------------------
# STEP 3: LOAD TO DATABASE
# ----------------------------
conn = sqlite3.connect(db_name)# Establish a connection to the SQLite database specified by 'db_name'. If the database file does not exist, it will be created. This connection object 'conn' will be used to execute SQL commands and manage the database operations.
df.to_sql(table_name, conn, if_exists='replace', index=False)# Save the DataFrame to a table in the SQLite database. The table will be named according to 'table_name'. If a table with the same name already exists, it will be replaced. The index of the DataFrame will not be saved as a column in the database.    
conn.close()# Close the connection to the SQLite database to free up resources and ensure that all changes are saved properly.

print("✅ Data saved to CSV and SQLite DB")# Print a confirmation message indicating that the data has been successfully saved to both the CSV file and the SQLite database.