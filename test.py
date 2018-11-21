# -*- coding: utf-8 -*-
from flask import Flask, current_app

app = Flask(__name__)

with app.app_context():
    a = current_app
    print(a)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# ctx.pop()




