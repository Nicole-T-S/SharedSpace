from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True) 