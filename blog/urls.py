from django.urls import path
from blog.views import index, site

urlpatterns = [

    path("hello/", index),

    path("", site)

]