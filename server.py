#!/usr/bin/python
from flask import Flask, render_template, send_from_directory, request

from db_functions import get_unique_patronyms, get_unique_first_names, get_unique_last_names, \
    get_awards_list, get_unique_awards

app = Flask(__name__)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route("/")
def main():
    print request
    return render_template('template.html',
                           awards=get_unique_awards(),
                           awarded_people=get_awards_list(),
                           unique_last_names=get_unique_last_names(),
                           unique_first_names=get_unique_first_names(),
                           unique_patronyms=get_unique_patronyms())


if __name__ == '__main__':
    app.run(debug=True)
