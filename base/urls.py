from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import app.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", app.views.index, name="index"),
    path("register/", app.views.register, name="register"),
    path("login/", app.views.login, name="login"),
    path("order/", app.views.order, name="order"),
    path("db/", app.views.db, name="db"),
    path("admin/", admin.site.urls),
]
