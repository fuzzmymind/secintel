from django.shortcuts import render, HttpResponse
from .forms import AnalyzeUrlForm
import json

def url_home(request):
    # if request.method == "GET":
        # form = AnalyzeUrlForm()
    context = {}
    return render(request, 'analyze_url.html', context)
    

def url_analyze(request):
    url = request.POST["url"]
    result = {
        "key": url
    }
    return HttpResponse(json.dumps(result), content_type="application/json"
)
