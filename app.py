from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load data from Excel file
df = pd.read_excel('data.xlsx')
authors = df["Author's name"].tolist()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/search')
def search():
    query = request.args.get('q').lower()
    results = [author for author in authors if query in author.lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
