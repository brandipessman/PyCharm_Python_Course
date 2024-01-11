import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENTID = "c957a9feeda34f61a04eb046f98172fe"
CLIENTSECRET = "f6c7469770514a358d7246c06cc6dce0"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "http://example.com",
        client_id = CLIENTID,
        client_secret =CLIENTSECRET,
        show_dialog = True,
        cache_path="token.txt",
        username = "bjpessman-gb"
    )
)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
spotify_webpage = response.text

soup = BeautifulSoup(spotify_webpage, "html.parser")
titles = soup.select("li #title-of-a-story")
list = []
for title in titles:
    list.append(title.getText().strip())

uris = []
for title in list:
    result = sp.search(q = f"track:{title}", type = "track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in spotify. Skipped.")

playlist = sp.user_playlist_create(user = user_id, name = f"Top 100 From {date}", public = False)
sp.playlist_add_items(playlist_id = playlist["id"], items = uris)


