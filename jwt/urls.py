from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    # django admin 페이지 (미사용)
    # path('admin/', admin.site.urls),
    
    path('', include('backend.urls')),
]
