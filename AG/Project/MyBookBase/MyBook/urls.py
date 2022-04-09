
from django.contrib import admin
from django.urls import path,include

# from Blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('', include('Blog.urls'))
]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


