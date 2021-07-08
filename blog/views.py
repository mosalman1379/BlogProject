from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from blog.models import Post


# This function is another view of PostList class based view
def post_list(request):
    """
    this view functions show all post objects
    :param request:
    :return: all post objects
    """
    posts = Post.published.all()
    paginator = Paginator(posts, 3)  # 3 post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'posts': posts, 'page': page})


class PostList(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    context_object_name = 'posts'
    template_name = 'blog/list.html'


def post_detail(request, year, month, day, post):
    """
    this view function show specific post object with special attributes
    :param request: http request
    :param year: the year of published post
    :param month: the month of published post
    :param day: the day of published post
    :param post: the post for slug of published post
    :return: show object in html or raise 404 http error
    """
    post = get_object_or_404(klass=Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/detail.html', {'post': post})
