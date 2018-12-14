from django.conf.urls import url, include
from rest_framework import routers
from Board import views as board_views
from History import views as history_views
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'boards', board_views.BoardViewSet)
router.register(r'history', history_views.BoardHistoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]