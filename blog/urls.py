
from django.urls import path
from . import views
urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view(), name='home'),
    path('acm/', views.AcmView.as_view(), name='acm'),
    path('acm/<slug:slug>', views.AcmCodesView.as_view(), name='acm_codes'),
]
