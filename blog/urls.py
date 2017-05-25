from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.index, ),
    url(r'^blog/view/(?P<slug>[^\.]+)$', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+)$', views.view_category,  name='view_blog_category'),

                     ]
