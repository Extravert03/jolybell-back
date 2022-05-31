from rest_framework import routers

from . import views

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'category', views.ProductCategoryViewSet)

urlpatterns += router.urls
