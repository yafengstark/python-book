# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'

# 这是中文注释

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)