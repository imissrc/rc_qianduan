from django.urls import path

from . import views

urlpatterns = [
    path("",views.login),
    path("address_book/",views.address_book),
    path("register/",views.register),
    path("add_contactpeo/",views.add_contactpeo),
    path("saveinfo/",views.saveinfo),
    path("updateinfo/<int:infoid>",views.updateinfo),
    path("delinfo/<int:infoid>",views.delinfo),
    path("logout/",views.logout),
    path("search/",views.search),
]