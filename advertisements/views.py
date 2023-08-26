from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.core.handlers.wsgi import WSGIRequest
def index(requests):
    advertisements = Advertisement.objects.all()

    context = {
        "advertisements": advertisements
    }

    return render(requests, 'advertisements/index.html', context)



def top_sellers(requests):
    return render(requests, 'advertisements/top-sellers.html')

def advertisement_post(request: WSGIRequest):
    
    print(request.method)
    print(request.POST)
    print(request.FILES)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse("main-page")
            )
        else:
            print(form.errors)
    else:
        form = AdvertisementForm()
        
    context = {"form": form}
    return render(request, 'advertisements/advertisement-post.html', context)