from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = pageNotFound