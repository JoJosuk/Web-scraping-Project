import pandas as pd
from mypythonlib import scrape
from django.shortcuts import render
import json
# Create your views here.

table=pd.DataFrame()
def index(request):
    return render(request, 'core/index.html')
def itemgive(request):
    itemNames=request.GET.get('item')
    table=scrape.getdata(itemNames)
    json_records=table.reset_index().to_json(orient='records')
    arr=[]
    arr=json.loads(json_records)
    contextt={'d':arr}
    return render(request, 'core/itemgive.html',contextt)
def intermediate(request):
    keywords = request.GET.get('keywords')
    pricel=request.GET.get('pricel')
    priceh=request.GET.get('priceh')
    keywords=list(map(str,keywords.split()))
    sbtable=pd.read_excel('./data.xlsx')
    for i in keywords:
        sbtable=sbtable[sbtable['Description'].str.contains(i)]
    table=sbtable
    json_records=table.reset_index().to_json(orient='records')
    arr=[]
    arr=json.loads(json_records)
    contextt={'d':arr}
    return render(request, 'core/intermediate.html',contextt)