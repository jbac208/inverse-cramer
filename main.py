import requests

username = "jimcramer"

h = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAPYXBAAAAAAACLXUNDekMxqa8h%2F40K4moUkGsoc%3DTYfbDKbT3jJPCEVnMYqilB28NHfOPqkca3qaAxGfsyKCs0wRbw"
}

with requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=h) as r:
    guest_token = r.json()["guest_token"]
    h["x-guest-token"] = guest_token

    with requests.get(f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}", headers=h) as tr:
        data = tr.json()

        for tweet in data:
            # extract the properties
            print(f"{tweet['created_at']}: {tweet['text']}")
