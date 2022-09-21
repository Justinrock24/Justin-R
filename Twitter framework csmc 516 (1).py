#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import tweepy


# In[2]:


def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Tweet Text:{ith_tweet[2]}")
        print(f"Hashtags Used:{ith_tweet[3]}")


# In[3]:


def scrape(words, date_since, numtweet):

        db = pd.DataFrame(columns=['username','description','text','hashtags'])

        tweets = tweepy.Cursor(api.search_tweets,words, lang="en",since_id=date_since,tweet_mode='extended').items(numtweet)

        list_tweets = [tweet for tweet in tweets]
        print(list_tweets)
        i = 1
        for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                hashtags = tweet.entities['hashtags']


                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])


                ith_tweet = [username, description, text, hashtext]
                db.loc[len(db)] = ith_tweet

                printtweetdata(i, ith_tweet)
                i = i+1


# In[4]:


if __name__ == '__main__':


        consumer_key = "rsWNgTlQkE0HhiDHi3DxJjGc6"
        consumer_secret = "MZ7nhftytJdy5NsBFNJGjmhGmXkCWT74DmbTH7MJE8vIDWt56c"
        access_key = "1571650149742411777-EpiherGDvBdMQZxXvn5bFAAvlQGdnU"
        access_secret = "DWHGI6LNXVISc0OL2yWDbCO1fO5myrSBKNVh9gSxZGN0i"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        print("Enter Twitter HashTag to search for")
        words = input()
        print("Enter Date since The Tweets are required in yyyy-mm--dd")
        date_since = input()

        numtweet = 100
        scrape(words, date_since, numtweet)
        print('Scraping has completed!')

