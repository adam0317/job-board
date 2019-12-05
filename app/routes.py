from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
import requests
import datetime
import os

bp = Blueprint("all", __name__)

@bp.route('/')
def index():
  
  return render_template('home.html')  