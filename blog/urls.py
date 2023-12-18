from django.urls import path
from blog.views import main_page, goods

urlpatterns = [

    path("main_page/", main_page),


    path("main_page/<int:my_id>/", goods)

]
