from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ProductPageView

urlpatterns = [
    path('products/', ProductPageView.as_view(), name='products'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]