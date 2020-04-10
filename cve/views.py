from django.shortcuts import render, HttpResponse
import json
from .forms import CveSearchForm, CveProductForm
import pip._vendor.requests as requests

# Create your views here.
def cve_search(request):
    url = ''
    data = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CveSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cve = form.cleaned_data['cve']
            r = requests.get('http://cve.circl.lu/api/cve/' + cve)
            data = r.json()
            # return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CveSearchForm()
    
    context = {
        'form': form,
        'url': url,
        'data': data
    }
    return render(request, 'cve_search.html', context)


def cve_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        r = requests.get('http://cve.circl.lu/api/browse/')
        data = r.json()["vendor"]
            
    context = {
        'vendors': data
    }
    return render(request, 'cve_product.html', context)


def get_cve_product_vendor(request):
    pass


def get_product_for_vendor(request):
    vendor_name = request.GET["vendor"]
    products = []
    result = []
    r = requests.get('http://cve.circl.lu/api/browse/' + vendor_name)
    products = r.json()["product"]
    for product in products:
        result.append({"name": product})
    return HttpResponse(json.dumps(result),content_type='application/json')


def cve_last_30(request):
    r = requests.get('http://cve.circl.lu/api/last/')
    data = r.json() 
    context = {
        'data': data
    }
    return render(request, 'cve_last_30.html', context)