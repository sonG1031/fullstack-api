import pandas as pd
import requests


if __name__ == "__main__":
    movies_df = pd.read_csv("data/movies.csv")
    movies_df['movieId'] = movies_df["movieId"].astype(str)
    
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(links_df, on='movieId', how="left")
    print(merged_df)