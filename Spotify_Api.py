from urllib.parse import urlencode
import requests

# token for spotify api

api_token = "https://accounts.spotify.com/api/token"

# insert of credentials

auth_response = requests.post(api_token, {
    'grant_type': "client_credentials",
    'client_id': "Insert Client ID here",
    'client_secret': "Insert Client Secret here",
})

# authentication

access_token = auth_response.json()['access_token']
headers = dict(Authorization=f"Bearer {access_token}")

# search'bar'

artist = input("artist to search for: ")
api_link = "https://api.spotify.com/v1/"

# search query

query = {
    "q": artist,
    "type": "artist",
    "limit": "7",
}

endpoint = "search?"

response = requests.get(f"{api_link}{endpoint}{urlencode(query)}", headers=headers).json()

# layout + output

print("________________________________________________________________________________________________________________"
      "_________________________________________")

print()

print('Name' + '                /                   ' + 'Genre' + '                /                   ' + 'Popularity')

print()

for artists in response["artists"]["items"]:
    print(f"{artists['name']} / {artists['genres']} / {artists['popularity']}")

print("________________________________________________________________________________________________________________"
      "_________________________________________")
