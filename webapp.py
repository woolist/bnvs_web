from flask import Flask, request, render_template, jsonify
import sys
import io
import contextlib
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/dl")
def dl():
    return render_template('digitalliteracy.html')

@app.route("/aisolution")
def aisolution():
    return render_template('aisolution.html')

@app.route("/digitaltransform")
def dt():
    return render_template('digitaltransform.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route("/blog-details")
def blog_details():
    return render_template('blog-details.html')

@app.route("/model-details")
def model_details():
    return render_template('model-details.html')

app.run(debug=True)