from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users_urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ]
