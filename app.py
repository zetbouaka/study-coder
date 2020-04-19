import traceback
import os

from flask import Flask, request, url_for, jsonify
from functools import wraps
import requests
import random

app = Flask(__name__)

@app.route('/leetcode', methods=['GET'])
def leetcode():
    URL = 'https://leetcode.com/api/problems/favorite_lists/top-interview-questions/'
    response = requests.get(URL)
    json = response.json()
    problems = json["stat_status_pairs"]

    a = 0
    b = len(problems)

    pick = random.randint(a, b)
    URL = f'https://leetcode.com/problems/{problems[pick]["stat"]["question__title_slug"]}'
    return f'<a href = "{URL}">오늘의 문제는 뭘까요?</a>'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
