Google Play Reviews Scraper

A Python script to search for apps on the Google Play Store, scrape all reviews for a selected app based on user inputs for language and country, and save the reviews into a database using a custom storage model.

Features

Search for apps on Google Play by name.

Scrape all user reviews for the selected app.

Supports specifying the country and language for reviews.

Saves reviews into a database through a modular models interface.

Includes configurable delay between requests to respect API rate limits.
Requirements

Python 3.7+

google-play-scraper

Your custom storage module for database operations (ensure it has connect_db(), insert_review(), and close_connection() functions).

Install the scraper dependency via pip:

pip install google-play-scraper

Usage

Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo


Run the script:

python your_script.py


When prompted:

Enter the name of the app to search for.

Enter the country code (e.g., us, tz) to scrape reviews from.

Enter the language code (e.g., en) to scrape reviews in.

The script will search for the app, fetch all reviews, and save them to your database.

Example
Search app to scrap: WhatsApp
Enter country code to scrape (e.g., 'us', 'tz'): us
Enter language code to scrape (e.g., 'en'): en
Inserted 3500 reviews into the database for app com.whatsapp.

Notes

The script uses a delay (sleep_milliseconds=1800) between review requests to avoid hitting Google Play rate limits.

Make sure your storage.models module is properly configured to connect and insert data into your database.

Currently, the script fetches reviews from the first search result. You can customize it to handle multiple results if needed.

License

MIT License
