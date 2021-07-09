from django.urls import path

from blog.views import post_detail, PostList, post_share

app_name = 'blog'

urlpatterns = [
    # path('', post_list, name='post_list'),
    path('', PostList.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/', post_share, name='post_share')
]
