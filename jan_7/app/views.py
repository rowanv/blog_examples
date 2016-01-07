from flask import render_template
from app import app

@app.route('/')
def sparklines_stock_dash():
    return render_template('index.html')
