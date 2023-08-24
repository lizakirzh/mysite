from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(requests):
    advertisements = Advertisement.objects.all()

    context = {
        "advertisements": advertisements
    }

    return render(requests, 'index.html', context)



def top_sellers(requests):
    return render(requests, 'top-sellers.html')

def post_adv(requests):
    form = AdvertisementForm()
    context = {"form": form}
    return render(requests, 'advertisement-post.html', context)