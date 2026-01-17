import json
import pandas as pd

#complete Dataframe
com_df= pd.read_json("NLP_St\data\Movie_Ratings\movie_reviews.json")

#Dataframe that will be used
df_use = com_df[["genre_ids", "overview", "title"]]

#Genre-id DF
gid_df = pd.read_json("NLP_St\data\Movie_Ratings\genres_id.json")
gid_list = list(gid_df["id"])

print(df_use["overview"][4])