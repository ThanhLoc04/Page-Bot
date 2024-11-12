import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def execute():
    # Define the URL to scrape for EPL news
    url = "https://www.bbc.com/sport/football/premier-league"
    
    # Send HTTP request to the URL
    response = requests.get(url)

    # Check if the page is accessible
    if response.status_code != 200:
        return "⚠️ Unable to access the EPL website at the moment. Please try again later."
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all news articles (BBC website structure may change, so this selector is based on current structure)
    news_articles = soup.find_all('a', class_='gs-c-promo-heading')

    # Check if there are any news articles
    if not news_articles:
        return "⚠️ No latest news found."

    # Collect the titles and links to the news articles
    news_list = []
    for article in news_articles[:5]:  # Limit to the first 5 articles
        title = article.get_text().strip()
        link = article['href']
        # Ensure the link is a full URL
        full_link = urljoin(url, link)
        news_list.append(f"🔹 {title} - [Read More]({full_link})")

    # Format the output
    response = "⚽ **Latest EPL News** ⚽\n\n"
    response += "\n".join(news_list)

    # Fetch live matches if available
    live_matches_url = "https://www.bbc.com/sport/live/football"
    live_response = requests.get(live_matches_url)
    
    if live_response.status_code == 200:
        live_soup = BeautifulSoup(live_response.text, 'html.parser')
        live_matches = live_soup.find_all('a', class_='qa-match-block')

        if live_matches:
            response += "\n\n🔥 **Live Matches** 🔥\n"
            for match in live_matches[:3]:  # Limit to 3 live matches
                match_info = match.get_text().strip()
                response += f"⚡ {match_info}\n"
        else:
            response += "\n\n🔥 No live matches currently."

    return response
