from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('city/', views.CityView.as_view(), name='city'),
    path('city/<int:city_id>/street/', views.StreetView.as_view(), name='street'),
    path('shop/', views.ShopView.as_view(), name='shop')
]
