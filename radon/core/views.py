import pandas as pd
from mypythonlib import scrape
from django.shortcuts import render
import json
# Create your views here.

table=None
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