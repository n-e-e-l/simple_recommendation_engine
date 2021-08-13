from flask import Flask, render_template, request
#import pickle
#import numpy as np
import pandas as pd
from simple_recommendation import res
data_file = pd.read_csv(open('movies_sorted.csv', 'rb'))
from platform import python_version

print(python_version())
app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['num_movies']
    #temp=res(int(data1))
    temp = data_file[['title', 'vote_count', 'vote_average', 'score']].head(int(data1))
    temp.columns = ['Movie Title', 'Total Number of Votes', 'Average Votes', 'Score']
    temp.reset_index(inplace=True)
    temp.index += 1
    #print(temp)
    return render_template('after.html', tables=[temp.to_html(classes='data table table-striped table-bordered', header="true")], numm=int(data1))


if __name__ == "__main__":
    app.run(debug=True)
