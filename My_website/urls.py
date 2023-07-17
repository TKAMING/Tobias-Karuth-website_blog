from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import blog
from whoami.views import whoami
from contact.views import contact
from imprint.views import imprint
from test.views import test

urlpatterns = [
    path("", whoami, name="whoami"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("imprint/", imprint, name="imprint"),
    path("admin/", admin.site.urls),
    path("3.14159/", 3.14159, name="3.14159"),
]

urlpatterns += staticfiles_urlpatterns()