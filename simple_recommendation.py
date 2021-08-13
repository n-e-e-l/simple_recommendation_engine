import pandas as pd
def res(num):
    df_movies_metadata = pd.read_csv(r"H:\data_test_model_set\latest_check\portfolio\proj1\data\movies_metadata.csv", low_memory=False)
    C = df_movies_metadata['vote_average'].mean()
    m = df_movies_metadata['vote_count'].quantile(0.90)
    top_movies = df_movies_metadata.copy().loc[df_movies_metadata['vote_count'] >= m]
    # Calculation based on the IMDB formula
    top_movies["score"] = (top_movies['vote_count']/(top_movies['vote_count']+m) * top_movies['vote_average']) + (m/(m+top_movies['vote_count']) * C)
    top_movies.sort_values('score', ascending=False, inplace=True)
    top_movies.reset_index(inplace=True)
    top_movies.index += 1
    return (top_movies[['title', 'vote_count', 'vote_average', 'score']].head(num))