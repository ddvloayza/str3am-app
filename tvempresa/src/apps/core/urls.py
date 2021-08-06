from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [

    url(r'^utils/',
        include([
            url(r'^status-task/$',
                views.StatusTaskAPIView.as_view(),
                name="status-task"),
        ])),

]

urlpatterns = format_suffix_patterns(urlpatterns)
