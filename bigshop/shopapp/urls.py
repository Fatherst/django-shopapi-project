from django.urls import path
from .views import ListProductsView, ListCategoriesView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/popular/', ListProductsView.as_view(), name="index"),
    path('categories/', ListCategoriesView.as_view(), name="cats")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)