from os import name
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name='home'),
    path('searchresult',views.searchresult,name="searchresult")
     
    
    

]
urlpatterns+=staticfiles_urlpatterns()
