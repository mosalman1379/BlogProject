from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import post_detail, post_share, post_list, ListPosts, CommentViewSet

app_name = 'blog'
# used for support all 4 main action of api
router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', post_list, name='post_list'),
    # path('', PostList.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/', post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('api/v1/', ListPosts.as_view(), name='show-post-api'),
    path('api/v2/', include(router.urls), name='view-set-comment')
]
