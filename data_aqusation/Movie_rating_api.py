import requests
import json

url = "https://api.themoviedb.org/3/genre/movie/list?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

response = requests.get(url)
data = response.json()

with open("NLP_St\data\Movie_Ratings\genres_id.json", "w") as f:
  json.dump(data, f, indent=4)