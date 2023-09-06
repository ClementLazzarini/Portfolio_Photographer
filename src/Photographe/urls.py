from django.urls import path
from Photographe.views import home, portfolio, tarif, presentation, contact, mentions
from Portfolio import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('tarif/', tarif, name='tarif'),
    path('presentation/', presentation, name='presentation'),
    path('contact/', contact, name='contact'),
    path('mentions/', mentions, name='mentions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
