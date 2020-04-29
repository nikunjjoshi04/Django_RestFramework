from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', views.api_root),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('snippets/', snippet_list, name='snippets-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('users/', user_list, name='users-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
]
