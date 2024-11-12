import requests
from bs4 import BeautifulSoup
import random

def execute():
    # Scrape quotes from the website
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        return f"⚠️ Unable to access the quotes website at the moment. Error: {str(e)}"
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        return "⚠️ No quotes found on the page."

    # Randomly select a quote
    selected_quote = random.choice(quotes)
    quote_text = selected_quote.find("span", class_="text").get_text()
    author = selected_quote.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in selected_quote.find_all("a", class_="tag")]

    # Format the quote in a visually appealing way
    response = (
        f"🌟 **Inspiring Quote of the Moment** 🌟\n\n"
        f"\"{quote_text}\"\n\n"
        f"— **{author}**\n\n"
        f"🔖 **Tags**: {', '.join(tags) if tags else 'No tags available'}\n\n"
        f"💬 _Remember, a quote a day keeps negativity away!_ 💫"
    )

    return response
