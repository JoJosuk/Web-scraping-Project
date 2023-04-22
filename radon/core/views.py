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
    print(sbtable.dtypes)
    for i in keywords:
        sbtable=sbtable[sbtable['Description'].str.contains(i)]
    sbtable=sbtable[(sbtable['Price'] > min_price) & (sbtable['Price'] <= max_price)]
    table=sbtable
    json_records=table.reset_index().to_json(orient='records')
    arr=[]
    arr=json.loads(json_records)
    contextt={'d':arr}
    return render(request, 'core/intermediate.html',contextt)