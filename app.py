import requests
import random
import time
import os

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

quotes = [
    "Peace begins when you stop chasing chaos",
    "Silence is better than fake love",
    "Not everyone deserves your energy",
    "Self-respect looks like distance",
    "You outgrow what once broke you",
    "Some endings are quiet victories",
    "Protect your peace at all costs",
    "Growth requires uncomfortable goodbyes",
    "Your healing is your responsibility",
    "Let them miss the version of you they lost",
    "Distance reveals the truth",
    "Choose yourself without apology",
    "You deserve calm, not confusion",
    "Walking away is also strength",
    "Some people are lessons, not lifetimes",
    "You are allowed to start over",
    "Respect your own boundaries first",
    "Peace feels better than revenge",
    "You can love and still leave",
    "Not every connection is meant to last"
]

emojis = ["🖤", "✨", "🌙", "💭", "🕊️", "💔", "🌱", "🔥", "💫", "🤍"]

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    requests.post(url, data=payload)

while True:
    quote = random.choice(quotes)
    emoji = random.choice(emojis)
    message = f"{quote} {emoji}"

    print("Posting:", message)
    post_to_facebook(message)

    # attendre 90 minutes
    time.sleep(5400)
