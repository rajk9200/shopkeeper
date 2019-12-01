
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('register/', include('register.urls')),
    path('accounts/', include('accounts.urls')),
]

