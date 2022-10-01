from django.urls import path,include
from first_app import views

app_name = 'first_app'

urlpatterns=[

     
     path("about/",views.about,name='about'),
     
     #path("",views.relative,name='relative'),
     
]