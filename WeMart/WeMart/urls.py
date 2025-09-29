
from django.contrib import admin
from django.urls import path, include
from user_app.api import urls as user_api_urls

import user_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(user_api_urls)),
]
