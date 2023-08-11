#DAY 36 STOCK TRADING API + TWILIO
import requests
from twilio.rest import Client

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "AMCU1FA9NTAHWS40"
NEWS_API_KEY = "d9c4d0ef60ac432192b9ca3eaacc540e"
TWILIO_SID = "AC3743a65d0a35ea194d8946ce546f6c15"
TWILIO_AUTH_TOKEN = "1d2b5e2bf5b8a223eff7ba6c5b0310cd"

#1. - Get yesterday's closing stock price. 
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "AAPL",
    "apikey" : STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print("Yesterday's Closing price was: $", yesterday_closing_price)


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print("Day Before Yesterday's Closing price was: $", day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between
price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference 
percent_diff = round((price_difference / float(yesterday_closing_price)) * 100, 1)
print(percent_diff,"%") 


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percent_diff) > 0:
    news_params = {
    "apiKey" : NEWS_API_KEY, 
    "q": COMPANY_NAME,
    }

#TODO 6. - News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
  
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles
    one_article = articles[:1]
    print(one_article)

#TODO 8. - Create a new list of the first 3 article's headline and description
    articles_formatted= [f"{STOCK_NAME}: {up_down}{percent_diff}%\n Headline: {article ['title']}. \nBrief: {article ['description']}" for article in one_article]
    
#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in articles_formatted:
        message = client.messages.create(    
            body= article,          
            to = "+16474480857",
            from_ = "+14708023795"
                   
        )




#Message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



