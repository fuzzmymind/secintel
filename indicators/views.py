from django.shortcuts import render, HttpResponse
from .forms import AnalyzeUrlForm
import pip._vendor.requests as requests
import json
import os

def url_home(request):
    # if request.method == "GET":
        # form = AnalyzeUrlForm()
    context = {}
    return render(request, 'analyze_url.html', context)
    

def url_analyze(request):
    url = request.POST["url"]
    api_key = os.getenv('VT_API_KEY')
    headers = {
        "x-apikey": api_key
    }
    result = None
    r = requests.get('https://www.virustotal.com/api/v3/urls/'+ url, headers=headers)
    if r.status_code == 200: 
        result = r.json()
    else:
        result = "No data found"
    return HttpResponse(json.dumps(result), content_type="application/json"
)


def domain_analyze(request):
    context = None
    return render(request, 'analyze_domain.html', context)
