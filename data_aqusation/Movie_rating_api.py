import requests
import json
import time

base_url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page="

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkOTcwNjBkYjYzY2ViMTZiYWQwNGE4YjQ5NWNjMjFkNSIsIm5iZiI6MTc2ODUwNDQ5NS4xMzYsInN1YiI6IjY5NjkzY2FmMDQ0NmZkMzdkMTIzNmQ0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.V8DxyqCCuINIBZxYzVxHDvE17NBldUlHTBfGEu-MxEM"
}


all_movies = [] 

for i in range(9, 11):
  response = requests.get(base_url + str(i), headers=headers)
  data = response.json()
    
  if "results" in data:
    all_movies.extend(data["results"])
    
  print(f"Fetched page {i}, total movies so far: {len(all_movies)}")
  time.sleep(2.0)


with open(r"NLP_St\data\Movie_Ratings\movie_review_all8.json", "w", encoding="utf-8") as f:
  json.dump(all_movies, f, indent=4, ensure_ascii=False)

print("All done - Antas.")
