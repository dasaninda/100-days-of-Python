if percent_diff > 5:
    news_params = {
    "apiKey" : NEWS_API_KEY, 
    "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
    print(articles)