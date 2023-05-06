import requests
from flask import Flask, render_template

app = Flask(__name__)

username = "jimcramer"

h = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw"
}

def create_tweet_link(username,tweet_id):
  """
  This function takes username and tweet_id of a tweet and returns a link for the tweet.
  Parameters
  ----------
  username : username for the tweet(string)
  tweet_id : unique tweet id associated with each twitt.  (string)
  """
  return f"https://twitter.com/{username}/status/{tweet_id}"

with requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=h) as r:
    guest_token = r.json()["guest_token"]
    h["x-guest-token"] = guest_token

    with requests.get(f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}", headers=h) as tr:
        data = tr.json()

@app.route("/")
def index():
    # Get tweet HTML strings for latest 5 tweets
    tweet_html_list = []
    for tweet in data[:5]:
        tweet_url = create_tweet_link(username, tweet['id'])
        api_url = f"https://publish.twitter.com/oembed?url={tweet_url}&hide_thread=true"
        response = requests.get(api_url)
        tweet_html = response.json()["html"]
        tweet_html_list.append(tweet_html)
    
    # Render template with tweet HTML strings
    return render_template("index.html", tweet_html_list=tweet_html_list)


if __name__ == "__main__":
    app.run(debug=True)
