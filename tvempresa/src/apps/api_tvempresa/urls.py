from django.urls import path
from django.conf.urls import url


from rest_framework import routers
from .viewsets import CapitulosViewSet, ProgramasViewSet, SearchCapituloList, HomeViewSet
app_name = 'api_tvempresa'

router = routers.SimpleRouter()
router.register('api_capitulos_tvempresa', CapitulosViewSet)
router.register('api_programas_tvempresa', ProgramasViewSet)
router.register('api_search_capitulos', SearchCapituloList)
router.register('api_home_video', HomeViewSet)

urlpatterns = router.urls
