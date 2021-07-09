from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.forms import EmailPostForm
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


def post_share(request, post_id):
    post = get_object_or_404(klass=Post, pk=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} recommends you read {post.title}'
            message = f'Read {post.title} as {post_url}\n\n{cd["name"]}\'s comments: {cd["comments"]}'
            send_mail(subject, message, 'mosalman1379@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', context={'post': post, 'form': form, 'sent': sent})
