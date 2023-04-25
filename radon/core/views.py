import pandas as pd
from mypythonlib import scrape
from django.shortcuts import render
import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def index(request):
    return render(request, 'core/index.html')
def itemgive(request):
    itemNames=request.GET.get('item')
    table,cou=scrape.getdata(itemNames)
    # cou=json.dumps(cou, indent = 4) 
    json_records=table.reset_index().to_json(orient='records')
    arr=[]
    arr=json.loads(json_records)
    fig = px.histogram(table, x='Price',title='Price Distribution',color_discrete_sequence=['#EC4020'])
    fig.update_traces(marker_line_color='black',marker_line_width=1.5, opacity=0.75)  
    chart=fig.to_html()
    plt2=px.bar(table,x='Price',y='Name',title='Price vs Name',color_discrete_sequence=['#EC4020'])
    plt2.update_layout(
        yaxis=dict(
            tickangle=-45,
            tickfont=dict(size=6),
            automargin=True
        )
    )
    chart2=plt2.to_html()
    contextt={'d':arr,'chart':chart,'chart2':chart2,'cou':cou}
    return render(request, 'core/itemgive.html',contextt)
def intermediate(request):
    sbtable=pd.read_excel('./data.xlsx')
    keywords = request.GET.get('keywords')
    min_price=request.GET.get('pricel')
    max_price=request.GET.get('priceh')
    if min_price=='':
        min_price=0
    if max_price=='':
        max_price=float(max(sbtable['Price']))
    min_price,max_price=float(min_price),float(max_price)
    keywords=list(map(str,keywords.split()))
    sbtable['Price']=sbtable['Price'].astype(float)
    for i in keywords:
        sbtable=sbtable[sbtable['Description'].str.contains(i)]
    sbtable=sbtable[(sbtable['Price'] > min_price) & (sbtable['Price'] <= max_price)]
    table=sbtable
    json_records=table.reset_index().to_json(orient='records')
    arr=[]
    arr=json.loads(json_records)
    contextt={'d':arr}
    return render(request, 'core/intermediate.html',contextt)