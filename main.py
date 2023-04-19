import tweepy
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

# API Keys and Access Keys
api_key = input("Enter API Key: ")

api_secret = input("Enter API Key Secret: ")

access_token = input("Enter Access Token: ")

access_token_secret = input("Enter Access Token Secret: ")

# Initialise OAuth1UserHandler
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret
)

# Create Tweepy API object
api = tweepy.API(auth)

# User specifies range between lines 26-29
def main():
    start_year = int(input("Enter the earliest year: "))
    start_month = int(input("Enter the earliest month: using 1 as January and 12 as December: "))
    end_year = int(input("Enter the latest year: "))
    end_month = int(input("Enter the latest month, using 1 as January and 12 as December: "))
    start_date = utc.localize(datetime(start_year, start_month, 1, 0, 0, 0))
    end_date = utc.localize(datetime(end_year, end_month, 31, 23, 59, 59))
    confirm = input("ARE YOU SURE YOU WANT TO DO THIS?\n") # Confirmation lol
    if confirm.lower() == "yes":
        for tweet in tweepy.Cursor(api.user_timeline).items(): # Retreive all tweets made by user
            if (tweet.created_at >= start_date) and (tweet.created_at <= end_date):
                api.destroy_status(tweet.id) # Deletes all tweets created within specified range
                # Status messages
                print("Tweet Deleted Successfully")
        print("Tweets Deleted Successfully.") 

    else:
        exit()

if __name__ == "__main__":
    main()