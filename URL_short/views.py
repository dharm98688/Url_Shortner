from django.shortcuts import render
import pyshorteners
from django.contrib import messages
# Create your views here.


def short(request):
    short= ""
    url = ""
    if request.method == "POST":
        url = request.POST['url']
        s = pyshorteners.Shortener()
        short = s.tinyurl.short(url)
        messages.success(request, "Url Short Generated")

    return render(request, "short.html", {'short': short, 'url': url})