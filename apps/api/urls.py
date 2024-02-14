from django.urls import path, include
from rest_framework import routers

from .views import CompanyViewSet, TecnicoList, PedidoViewSet


router = routers.DefaultRouter()

router.register(r'company', CompanyViewSet, basename='company')
router.register(r'v1/pedido', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/tecnicos', TecnicoList.as_view()),
]
