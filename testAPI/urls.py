"""testAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic import TemplateView
from testAPI import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/article/(?P<pk>[0-9]+)/comments/$', views.api_getCommentsByArticle, name='api-article-key'),
    url(r'^api/articles/$', views.api_putArticle, name='api-article-add'),
    url(r'^api/comment/(?P<pk>[0-9]+)/comments/$', views.api_getCommentsByComment, name='api-comment-key'),
    url(r'^api/comments/$', views.api_putComment, name='api-comment-add'),
]
