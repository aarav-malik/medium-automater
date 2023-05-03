import openai
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()


openai.api_key = "{}".format(os.environ.get('OPENAI_API_KEY'))

#def search_popular_topics():



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
        "Authorization": "Bearer {}".format(os.environ.get('API_KEY')),
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
        "https://api.medium.com/v1/users/{}/posts".format(os.environ.get('CLIENT_ID')), headers=headers, json=data
    )
    if response.status_code == 201:
        print(f"Article about {topic} posted on Medium!")
    else:
        print(f"Error posting article about {topic} on Medium: {response.text}")

topics = ["Hello"]
for topic in topics:
    article = generate_article(topic)
    post_article_on_medium(topic, article)