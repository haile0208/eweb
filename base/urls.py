from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('',views.HomeView.as_view(), name="index") ,
    path('index',views.HomeView.as_view(), name="index"),
    path('sales',views.sales, name="sales"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('product/<slug>/',views.ItemDetailView.as_view(), name = 'product'),
]

