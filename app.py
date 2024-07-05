from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    today = date.today().strftime("%Y-%m-%d")
    return jsonify({"date": today})

if __name__ == '__main__':
    app.run(debug=True)
