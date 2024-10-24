# eBay Review Scraper for Samsung Galaxy Phones

This Python script scrapes product reviews from eBay for different versions of Samsung Galaxy phones and saves them in separate text files. It uses the `requests` library to retrieve web pages and `BeautifulSoup` for parsing the reviews.


## Chosen Products

The script collects reviews for the following Samsung Galaxy versions:

1. **Samsung Galaxy S20**  
2. **Samsung Galaxy S21**  
3. **Samsung Galaxy S22**  
4. **Samsung Galaxy S23**

Each product has its own eBay review page, and the corresponding URLs are included in the script.


## How It Works

1. **Retrieves Web Page**: The `requests` library fetches the product review page for each Samsung Galaxy version.
2. **Parses Reviews**: The `BeautifulSoup` library parses the HTML content to extract reviews based on specific HTML tags and classes.
3. **Saves Reviews**: Reviews are saved into separate text files (one per product version).


## Instructions to Run

### Prerequisites:

- Install required libraries:
    ```bash
  pip install requests
  pip install beautifulsoup4
    ```

How to Run:
1. Download the script.
2. Open a terminal in the directory where the script is located.
3. Run the script with:
```bash
python scraper.py
```