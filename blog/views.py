from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def mifuncion(request):
    mensaje= "Gabriela"
    mensaje2 = "Sokayna"
    context = {}
    context['key']= Post.objects.all()

    return render(request, 'blog/index.html', context)


