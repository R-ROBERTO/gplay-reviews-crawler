from google_play_scraper import Sort, reviews_all, search
from storage import models

app = input("Search app to scrap: ")
search_result = search(
    app,
    lang="en",  # defaults to 'en'
    country="us",  # defaults to 'us'
)

if not search_result:
    print("No apps found for your query. Please try again.")
    exit()

# Connect to DB first
models.connect_db()

region = input("Enter country code to scrape (e.g., 'us', 'tz'): ")
language = input("Enter language code to scrape (e.g., 'en'): ")

app_id = search_result[0]['appId']

result = reviews_all(
    app_id,
    sleep_milliseconds=1800,
    lang=language,
    country=region,
)

for review in result:
    models.insert_review(review)

# Close connection when done
models.close_connection()

print(f"Inserted {len(result)} reviews into the database for app {app_id}.")
