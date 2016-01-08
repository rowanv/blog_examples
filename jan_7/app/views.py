import datetime
import requests
from flask import Response, render_template
import pandas as pd
from app import app
import json


@app.route('/')
def sparklines_stock_dash():
    return render_template('index.html')

@app.route('/data/not_realtime/currency_rates_month/')
def data_currency_rates_month_not_realtime():
    data = []
    with open('df_rates_month.json') as f:
        for line in f:
            data.append(json.loads(line))
    data = json.dumps(data[0])
    return Response(response=data,
                    status=200,
                    mimetype='application/json')


@app.route('/data/currency_rates_month/')
def data_currency_rates_month():
    base = datetime.datetime.today()
    datetime_list = [base - datetime.timedelta(days=x) for x in range(0, 30)]
    date_list = [datetime_obj.date().__str__() for datetime_obj in datetime_list]
    url_list = []

    for date in date_list:
        url_list.append('http://api.fixer.io/' + date + '?base=USD')

    json_objects = []
    for url in url_list:
        r = requests.get(url)
        json_objects.append(r.json())

    df_rates_month = pd.io.json.json_normalize(json_objects)
    json_response = df_rates_month.to_json()
    return Response(response=json_response,
                    status=200,
                    mimetype='application/json')
