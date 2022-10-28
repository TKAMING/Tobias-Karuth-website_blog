from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import blog
from whoami.views import whoami
from contact.views import contact

urlpatterns = [
    path("", whoami, name="whoami"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()