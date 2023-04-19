# TweetSweep
This Python code allows you to delete all tweets made by a Twitter user within a specified date range. The code uses the Tweepy library, which is a Python wrapper for the Twitter API, to access the user's tweets and delete them.

## How to Use
Before you can use this code, you need to create a Twitter Developer Account and obtain your API keys and access tokens. The code prompts the user to enter these credentials at the beginning of the script.

To use the code, run the script and follow the prompts. You will be asked to enter the earliest and latest year and month for the date range within which you want to delete tweets. Once you confirm that you want to proceed, the script will delete all tweets made by the specified user within the specified date range.

## Dependencies
This code requires the Tweepy library, which you can install using pip:

- python
- tweepy
<br>
The code also uses the following Python libraries, which are part of the standard library and do not need to be installed separately:

- datetime
- pytz
## Notes
This code will permanently delete all tweets made by the specified user within the specified date range. Use with caution.
The script deletes all tweets one by one, so it may take some time to delete all tweets if the user has a large number of tweets.
Twitter has rate limits on API requests, so if you have a large number of tweets to delete, you may need to run the script multiple times over a period of time.
At the moment, this script requires you to have a [Twitter Developer Account](https://developer.twitter.com/en), but this will be made for normal Twitter accounts to use in the near future.
