import praw
import json
import time

with open("config.example.json") as f:
    config = json.load(f)

reddit = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"],
    username=config["username"],
    password=config["password"],
)

def monitor_subreddit(AKnightoftheSeven):
    subreddit = reddit.subreddit(AKnightoftheSeven)
    for submission in subreddit.new(limit=10):
        # placeholder for moderation logic
        print(f"Checked submission: {submission.id}")

if __name__ == "__main__":
    for sub in config["subreddits"]:
        monitor_subreddit(sub)
    time.sleep(5)
