from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
import requests
import datetime
import os
import json
from html.parser import HTMLParser


bp = Blueprint("all", __name__)

@bp.route('/')
def index():
  with open('example.json') as json_file:
    jobs = json.load(json_file)
  # github_jobs = requests.get("https://jobs.github.com/positions.json")
  # jobs = json.loads(github_jobs.text)
  print(len(jobs))
  return render_template('home.html', jobs=jobs)  