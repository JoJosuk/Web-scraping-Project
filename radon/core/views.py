from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def itemgive(request):
    itemname=request.GET['item']
    return render(request, 'core/itemgive.html',{'itemname':itemname})