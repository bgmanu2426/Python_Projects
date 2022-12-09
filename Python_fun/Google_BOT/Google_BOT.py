import openai
import bs4
from bs4 import BeautifulSoup
import requests

green = '\x1b[32m'
white = '\x1b[37m'

# Insert your API key above
api_key = "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"
if not api_key:
    get_api_key_string = "Enter your OpenAPI key, available at https://beta.openai.com/account/api-keys: "
    api_key = input(get_api_key_string)
openai.api_key = api_key
completion = openai.Completion()


def get_questions_answers_so_far(questions, answers):
    convo = "Here is Alice and Jing\'s convo so far:\n"
    for question, answer in zip(questions, answers):
        convo += f"Jing: {question}\n"
        convo += f"Alice: {answer}\n"
    return convo


google_template = 'http://google.com/search?q='


def make_template1(question, convo):
    return f'''
Alice is an incredibly smart and nice software engineer with an interest in the news. She likes to use Google to help herself and her friends stay informed. Today, Alice and her friend Jing are chatting online. 
{convo}
Jing: {question}
Alice responds, "Let me look that up for you."
Alices navigates to {google_template}'''


def make_template2(html):
    return f'''
Alice sees this text from the Google search page:
```
"""
{html}
"""
```
From this, she concludes that the answer to her friend's question is:
'''


chat_log = ''


def predict(chat_log):
    response = completion.create(engine="text-davinci-003",
                                 prompt=chat_log,
                                 temperature=0.0,
                                 max_tokens=250,
                                 top_p=1.0,
                                 frequency_penalty=0.0,
                                 presence_penalty=-0.6)
    answer = response.choices[0].text.strip()
    return answer


questions, answers = [], []


def get_google_search_url(response):
    supplemented = google_template + response
    return supplemented[:supplemented.index(' ')]


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
    else:
        text = ""
    return text


def flow(chat_log):
    global questions
    global answers
    print(f'{white}')
    question = input('Question: ')
    chat_log += make_template1(
        question, get_questions_answers_so_far(questions, answers))
    questions.append(question)
    answers.append('')
    openai_response = predict(chat_log)
    google_url = get_google_search_url(openai_response)
    html = get_html(google_url)
    chat_log = chat_log.replace(google_template, google_url)
    chat_log += make_template2(
        html)
    answer = predict(chat_log)
    answers[-1] = answer
    return answer


for i in range(30):
    answer = flow(chat_log)
    print(f"{green}{answer}")
    chat_log = ''

query = "what has been happening in the news lately, according to Wikipedia?" #Use this query in the question to get the latest news from the whole world

# Search Wikipedia for recent news articles
wiki_url = "https://en.wikipedia.org/wiki/Special:Search?search=" + query
response = requests.get(wiki_url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Find the first link to a news article on the Wikipedia search results page
article_link = soup.find(
    "div", {"class": "mw-search-results"}).find("a")["href"]

# Retrieve the news article from Wikipedia
article_response = requests.get("https://en.wikipedia.org" + article_link)
article_soup = bs4.BeautifulSoup(article_response.text, 'html.parser')

# Parse the news article to extract the relevant information
title = article_soup.find("h1", {"id": "firstHeading"}).text
date = article_soup.find("li", {"id": "footer-info-lastmod"}).text
summary = article_soup.find(
    "div", {"class": "mw-parser-output"}).find("p").text

# Print the news article information
print("Title:", title)
print("Date:", date)
print("Summary:", summary)