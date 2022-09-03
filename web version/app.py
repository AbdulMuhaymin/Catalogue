from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


df = pd.read_csv('planets.csv')
 
 
@app.route('/')
def table():
    return render_template('index.html', tables=[df.to_html()], titles=[''])
 
 
if __name__ == "__main__":
    app.run(host="localhost")