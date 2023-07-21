from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return render(requests, 'index.html')



def top_sellers(requests):
    return render(requests, 'top-sellers.html')