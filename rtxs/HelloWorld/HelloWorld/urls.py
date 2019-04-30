from django.contrib import admin
from django.conf.urls import *
from django.urls import path
from HelloWorld import view, testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', view.hello),
    path('hello2/', view.hello2),
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
