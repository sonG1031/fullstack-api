import pandas as pd
import requests

def add_url(row):
    return f'https://www.imdb.com/title/tt{row}/'

def add_rating(df):
    ratings_df = pd.read_csv('data/ratings.csv')
    ratings_df['movieId'] = ratings_df['movieId'].astype(str)
    agg_df = ratings_df.groupby('movieId').agg(
        ratings_count = ('rating', 'count'),
        ratings_avg = ('rating', 'mean')
    ).reset_index()
    
    ratings_added_df = df.merge(agg_df, on='movieId')
    return ratings_added_df

if __name__ == "__main__":
    movies_df = pd.read_csv("data/movies.csv")
    movies_df['movieId'] = movies_df["movieId"].astype(str)
    
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(links_df, on='movieId', how="left")
    merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
    
    result_df = add_rating(merged_df)
    print(result_df)