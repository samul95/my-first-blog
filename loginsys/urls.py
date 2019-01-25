from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^addnewauth/', views.addnewauth, name='addnewauth'),
]