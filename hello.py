import openai
import requests
from bs4 import BeautifulSoup


openai.api_key = "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"

def search_popular_topics():
    # Search for popular topics using Google Trends
    url = "https://trends.google.com/trends/explore?date=today%201-m&geo=US"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    topics = soup.find_all("div", class_="label-text")
    return [topic.text for topic in topics]


def generate_article(topic):
    # Generate an article using ChatGPT

    prompt = f"You are a professional writer who would generate it in proper markdown formatting. is in the top 10% of medium writers so write an article about {topic} with code if needed. Should be like a standard medium post. Include Links as well if necessary. Format it properly."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    article = response.choices[0].text
    print(article)
    return article

def post_article_on_medium(topic, article):
    # Post the article on Medium
    headers = {
        "Authorization": "Bearer 2ea41f1ec870a60ac24293f8b2a61846e60253baeeb4a4f682ca672dfa2d8aa4f",
        "Content-Type": "application/json",
    }
    data = {
        "title": f"{topic} - AI.writer",
        "contentFormat": "markdown",
        "content": article,
        "tags": [], 
        "publishStatus": "draft",
    }
    response = requests.post(
        "https://api.medium.com/v1/users/1951b0de17806bb4ae5320bab533c6263ad44526daffad10434e0cc2603966c7d/posts", headers=headers, json=data
    )
    if response.status_code == 201:
        print(f"Article about {topic} posted on Medium!")
    else:
        print(f"Error posting article about {topic} on Medium: {response.text}")

# Search for popular topics
topics = []
# Generate an article and post it on Medium for each topic
for topic in topics:
    article = generate_article(topic)
    post_article_on_medium(topic, article)