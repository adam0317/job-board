from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
import requests
import datetime
import os
import json
from html.parser import HTMLParser


bp = Blueprint("all", __name__)

@bp.route('/')
def index():
  page = 0
  jobs_array = []
  results = True
  with open('example.json') as json_file:
    jobs = json.load(json_file)
  print(len(jobs))
  # while results:
  #   github_jobs = requests.get("https://jobs.github.com/positions.json?page={}".format(page))
  #   if not json.loads(github_jobs.text):
  #     results = False
  #   else:
  #     jobs_array.append(json.loads(github_jobs.text))
  #     page += 1
  #     print(len(jobs_array[page - 2]))
  return render_template('home.html', jobs=jobs)  