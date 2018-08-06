"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import CategoryList,SubCategoryList,ProductSubCategoryList,ProductCategoryList,InsertProduct

urlpatterns = [
	url(r'^category/', CategoryList.as_view()),   #API to get all categories 
	url(r'^subcategory/', SubCategoryList),   #API to get subcategories for a category 
    url(r'^products/', ProductSubCategoryList),  #API to get all products for a subcategory 
    url(r'^products_cat/', ProductCategoryList), #API to get all products for a category 
    url(r'^products_insert/', InsertProduct),  #API to post new product under existing subcategory and category
    url(r'^admin/', admin.site.urls),
]
