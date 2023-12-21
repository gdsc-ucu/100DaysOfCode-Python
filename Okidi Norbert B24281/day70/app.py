import tweepy

consumer_key = "fydT56wIaLDRRf69wVare3Kdd"
consumer_secret = "WdTIPWpDgQevvxVvT3I7k0xvaQ7Dpr5Zq8p7AAnvPipOm5xsOM"
access_token = "1295824232165842947-XeQhOgAwBjJdeAFv0pREbyO3AFtjb3"
access_token_secret = "tkPbPuBycadv3iTmvsnMS5jf0PwGx3bjWAKRIEDSaqe22"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

api.update_status("Hello, this is just another tweet")
 