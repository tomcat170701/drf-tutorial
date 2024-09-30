from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail
""" from rest_framework.routers import SimpleRouter """
""" from .views import UserViewSet, PostViewSet #viewsets """


""" router = SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls """


urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
