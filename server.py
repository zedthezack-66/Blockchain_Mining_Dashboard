 #(Optional) Set Up a Backend for Live Data
#For real-time data, run a Flask API that simulates mining stats.
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/stats')
def get_stats():
    return jsonify({"hash_rate": 50000.12, "blocks_mined": 12})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
   
