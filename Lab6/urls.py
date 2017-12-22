from django.conf.urls import url
from django.contrib import admin

from views import TovarView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', TovarView.as_view())
]
