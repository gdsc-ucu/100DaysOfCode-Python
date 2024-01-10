import tweepy
import random

consumer_key = "fydT56wIaLDRRf69wVare3Kdd"
consumer_secret = "WdTIPWpDgQevvxVvT3I7k0xvaQ7Dpr5Zq8p7AAnvPipOm5xsOM"
access_token = "1295824232165842947-XeQhOgAwBjJdeAFv0pREbyO3AFtjb3"
access_token_secret = "tkPbPuBycadv3iTmvsnMS5jf0PwGx3bjWAKRIEDSaqe22"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class SocialMediaBot:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data = {
            'posts': random.randint(0, 10),
            'likes': random.randint(0, 20),
            'comments': random.randint(0, 15),
        }

    def analyze_user_behavior(self):
        pass

    def make_recommendations(self):
        if self.user_data['likes'] > 10:
            return "You've been liking a lot of tweets lately. Check out these popular tweets!"

        if self.user_data['comments'] > 5:
            return "Your engagement through comments is great! Here are tweets that might interest you."

        if self.user_data['posts'] == 0:
            return "It seems you haven't tweeted anything yet. Share your thoughts with the community!"

        return "Here are some interesting tweets for you to explore."


user_id = '@OkidiNorbert'
social_bot = SocialMediaBot(user_id)

social_bot.analyze_user_behavior()

recommendation = social_bot.make_recommendations()
api.update_status(f"@{user_id} {recommendation}")