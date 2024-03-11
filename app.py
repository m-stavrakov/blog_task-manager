from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)

if __name__ == '__app__':
    app.run(debug=True, port=8080, threaded=True)

app.secret_key = 'twrgueyfig4tgg44tdfg212f'

@app.route('/')
def base():
    