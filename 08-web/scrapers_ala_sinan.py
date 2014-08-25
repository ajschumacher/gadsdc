###### begin stock scraper
import requests
from BeautifulSoup import BeautifulSoup

stock_ticker = 'ge'

base_url = "http://www.marketwatch.com/investing/stock/"                #base url for all stock quotes

r = requests.get(base_url + stock_ticker)                                 # create requests objects
soup = BeautifulSoup(r.text)                                            # create Beautiful Soup Object (note bs3 notation)

price =  float(soup.find('p', attrs={'class':'data bgLast'}).text)      # this pattern I found in the html

###### end stock scraper

###### begin twitter scraper

handle  = 'planarrowspace'                        
base_url = "https://twitter.com/"                     

r = requests.get(base_url + handle)
soup = BeautifulSoup(r.text)


#I found dates and contents seperately and in the end used a python command (zip) to put them together
tweet_dates =  soup.findAll('a', attrs={'class':'ProfileTweet-timestamp js-permalink js-nav js-tooltip'})
dates = [t['title'] for t in tweet_dates]

tweet_contents = soup.findAll('div', attrs={'class':'ProfileTweet-contents'})
contents = [t.findChild('p', attrs={'class':'ProfileTweet-text js-tweet-text u-dir'}).text for t in tweet_contents]

# at this point, contents holds a list of all tweets on page and dates holds a list of times represented as strings

dictionary_of_tweets = [{
    'tweet_contents':a,
    'tweet_date':b
  }
    for a, b in zip(contents, dates)
  ]


print dictionary_of_tweets

###### end twitter scraper
