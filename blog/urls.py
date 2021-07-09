from django.urls import path

from blog.views import post_detail, post_share, post_list

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    # path('', PostList.as_view(), name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/', post_share, name='post_share'),
    path('tag/<slug:tag_slug>/',post_list,name='post_list_by_tag')
]
