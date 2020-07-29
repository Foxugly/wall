from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from photologue.models import Gallery
from django.shortcuts import get_object_or_404, render


def homepage(request):
    galleries = Gallery.objects.all()
    return render(request, "homepage.html", {"galleries":galleries})

def  WallView(request, slug) :
    obj = get_object_or_404(Gallery, slug=slug)
    return render(request, "wall.html", {"obj":obj})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^photologue/', include('photologue.urls')),
    path('wall/<slug:slug>/', WallView, name="wall"),
    url(r'^$', homepage, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
