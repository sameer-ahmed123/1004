
from django.contrib import admin
from django.urls import path
from APP.views import emp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp',emp),
]
