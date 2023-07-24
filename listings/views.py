from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingsForm


def listing_list(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listing.html', context)


def listing_retrive(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/list.html', context)


def listing_create(request):
    form = ListingsForm()
    if request.method == 'POST':
        form = ListingsForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings')

    context = {
        'form': form
    }
    return render(request, 'listings/create.html', context)


def listing_update(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ListingsForm(instance=listing)
    if request.method == 'POST':
        form = ListingsForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings')

    context = {
        'form': form
    }
    return render(request, 'listings/update.html', context)


def listing_delete(request, pk):
    Listings.objects.get(id=pk).delete()
    return redirect('listings')
    