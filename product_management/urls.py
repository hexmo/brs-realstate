from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/<int:id>', views.view_details, name='view'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('comment/<int:id>', views.post_comment, name='comment'),
    path('create-post', views.create_post, name='create-post'),
    path('myListings', views.my_listings, name='myListings'),
    path('category/<str:type>', views.view_by_category, name='category'),
    path('search', views.search, name='search'), ]
