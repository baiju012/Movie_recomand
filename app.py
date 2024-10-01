from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset using Pandas
movies_df = pd.read_csv('imdb_top_1000.csv')

# Simple function to recommend movies by genre


def recommend_movies(genre):
    # Filter movies by genre (case-insensitive)
    filtered_movies = movies_df[movies_df['Genre'].str.contains(
        genre, case=False, na=False)]

    # Sort by IMDB Rating and return top 5 movies
    return filtered_movies[['Poster_Link', 'Series_Title', 'Released_Year', 'IMDB_Rating', 'Overview']].sort_values(by='IMDB_Rating', ascending=False).head(5)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        genre = request.form['genre']
        recommended_movies = recommend_movies(genre)
        return render_template('recommendations.html', movies=recommended_movies)


if __name__ == '__main__':
    app.run(debug=True)
