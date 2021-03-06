from __future__ import absolute_import

from django.conf.urls import url

from .endpoints import PagesAPIEndpoint, ImagesAPIEndpoint, DocumentsAPIEndpoint
from .router import WagtailAPIRouter


v1 = WagtailAPIRouter('wagtailapi_v1')
v1.register_endpoint('pages', PagesAPIEndpoint)
v1.register_endpoint('images', ImagesAPIEndpoint)
v1.register_endpoint('documents', DocumentsAPIEndpoint)

urlpatterns = [
    url(r'^v1/', v1.urls),
]
