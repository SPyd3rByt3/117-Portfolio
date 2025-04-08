from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about_page'),
    path("testing/", views.testing_view, name='testing_page'),
    path("contact/", views.contact_view, name='contact_page'),
]