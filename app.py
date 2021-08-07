
# Auther: James Landreth
# Date 7/25/2021
# Description: This program pulls wiki content based on a search
#               word

from flask import Flask, render_template, request, jsonify
import os
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    key_word = request.args.get("q")
    pull_page = requests.get("https://en.wikipedia.org/wiki/" + key_word)

    scraper = BeautifulSoup(pull_page.content, "html.parser")

    objects = scraper.find(id="mw-content-text")
    texts = objects.find_all('p', limit=5)
    return_dict = {"message": []}
    for i in range(5):
        return_dict["message"].append(texts[i].get_text())
        print(texts[i].get_text())

    return return_dict


if __name__ == "__main__":
    app.run(debug=True)

