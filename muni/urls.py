from django.conf.urls import url, include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Predios, limiteComunal
from .views import SimpleMapLayer
from djgeojson.views import TiledGeoJSONLayerView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='muni/predios.html'), name='muni'),
    url(r'^predios/$', GeoJSONLayerView.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios-hq'),
    url(r'^predios.simple/$', SimpleMapLayer.as_view(model=Predios, properties=('rol_manzan', 'numero_pre')), name='predios'),
    url(r'^conce/$', TemplateView.as_view(template_name='muni/limites.html'), name='conce'),
    url(r'^limites/$', GeoJSONLayerView.as_view(model=limiteComunal, properties=('zona')), name='limites-hq'),
    url(r'^limites.simple/$', SimpleMapLayer.as_view(model=limiteComunal, properties=('zona')), name='limites'),
    url(r'^limites/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
    TiledGeoJSONLayerView.as_view(model=limiteComunal), name='limites-tiled'),
]
