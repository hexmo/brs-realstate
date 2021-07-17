from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import datetime
from django.db.models import Q

# Create your views here.


def home(request):
    latest = Property.objects.order_by("created_at").reverse()[:4]
    sell_house = Property.objects.filter(type="Sell: House")[:4]
    sell_land = Property.objects.filter(type="Sell: Land")[:4]
    rent_house = Property.objects.filter(type="Rent: House")[:4]
    rent_land = Property.objects.filter(type="Rent: Land")[:4]
    params = {'latest': latest,
              'sell_house': sell_house, 'sell_land': sell_land, 'rent_house': rent_house, 'rent_land': rent_land}
    return render(request, 'home.html', params)


def view_details(request, id):
    product = Property.objects.get(id=id)
    comments = Comment.objects.filter(posted_on=product)
    similar = Property.objects.filter(type=product.type)[:4]
    params = {'product': product, 'similar': similar, 'comments': comments}
    return render(request, 'view.html', params)


@login_required(login_url='/login')
def delete(request, id):
    product = Property.objects.get(id=id)
    product.delete()
    return redirect(my_listings)


def view_by_category(request, type):
    products = Property.objects.filter(type=type)
    category = type
    params = {'products': products, 'category': category}
    return render(request, 'category.html', params)


@login_required(login_url='/login')
def my_listings(request):
    products = Property.objects.filter(owner=request.user)
    params = {'products': products}
    return render(request, 'my_listings.html', params)


@require_http_methods(["POST"])
@login_required(login_url='/login')
def post_comment(request, id):
    created_at = datetime.datetime.now()
    comment = request.POST['comment']
    owner = request.user
    product = Property.objects.get(id=id)
    comment_object = Comment.objects.create(
        owner=owner, created_at=created_at, posted_on=product, comment=comment)
    return redirect(view_details, id=id)


@require_http_methods(["GET"])
def search(request):
    key = request.GET['key']
    products = Property.objects.filter(
        Q(title__icontains=key) | Q(description__icontains=key))
    category = "Search results for " + key
    params = {'products': products, 'category': category}
    return render(request, 'category.html', params)


@ login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST' and request.FILES['cover']:
        title = request.POST['title']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        district = request.POST['district']
        description = request.POST['description']
        price = request.POST['price']
        type = request.POST['propertyType']
        cover = request.FILES['cover']
        # create object of Propery class
        property_object = Property.objects.create(title=title, address_1=address1, address_2=address2, district=district,
                                                  description=description, type=type, price=price, image=cover, created_at=datetime.datetime.now(), owner=request.user)
        # save it
        property_object.save()

        return render(request, 'create_listing.html')
    else:
        return render(request, 'create_listing.html')

# to update products


@login_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':
        product = Property.objects.get(id=id)
        product.title = request.POST['title']
        product.address_1 = request.POST['address1']
        product.address_2 = request.POST['address2']
        product.district = request.POST['district']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.type = request.POST['propertyType']
        # if image was updated
        if 'cover' in request.FILES:
            product.image = request.FILES['cover']

        product.save()
        return redirect(view_details, id=id)
    else:
        product = Property.objects.get(id=id)
        return render(request, 'update.html', {'product': product})
