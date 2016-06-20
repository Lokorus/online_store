from django.conf.urls import include, url
from django.contrib import admin
import social.apps.django_app.urls

urlpatterns = [
url(r'^', include('blog.urls')),
url(r'^admin/', include(admin.site.urls)),
]
