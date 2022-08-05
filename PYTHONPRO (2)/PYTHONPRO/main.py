from flask import Flask, Markup, render_template
import requests
import json
import time
from pymongo import MongoClient



app = Flask(__name__)

client = MongoClient('mongodb://gouravcharaya12:gouravcharaya1@ac-wftutd5-shard-00-00.1sudfex.mongodb.net:27017,ac-wftutd5-shard-00-01.1sudfex.mongodb.net:27017,ac-wftutd5-shard-00-02.1sudfex.mongodb.net:27017/?ssl=true&replicaSet=atlas-fp47j5-shard-0&authSource=admin&retryWrites=true&w=majority')
print(client)
db = client['hunny']
col = db["demoTestCollection11"]

sell = col.find_one()
# print(x)

# file = open('data.json')
# data = json.load(file)
clustered_labels = []
for x in sell['Worksheet']:
    if x not in clustered_labels:
        clustered_labels.append(x['category'])
filtered_clustered_labels = set(clustered_labels)
clustered_labels = list(filtered_clustered_labels)
labels = clustered_labels

clustered_list = []
for x in labels:
    price = 0
    for i in sell['Worksheet']:
        if i['category'] == x:
            price = price + float(i['sale_price'])
    clustered_list.append(price)
print(clustered_list)

values = clustered_list
#
#
colors = [
    "rgb(205, 92, 92)", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def bar_graph():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Big Basket Sales Price Per Category', max=3000, labels=bar_labels, values=bar_values)

@app.route('/line_graph')
def line_graph():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Reviews Per Category', max=3000, labels=line_labels, values=line_values)

@app.route('/pie_chart')
def pie_chart():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Market Price in USD', max=3000, set=zip(values, labels, colors))

@app.route('/demo')
def good():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
