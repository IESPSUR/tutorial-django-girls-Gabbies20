from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})


def mifuncion(request):
    mensaje= "Gabriela"
    mensaje2 = "Sokayna"
    context = {}
    context['key']= Post.objects.all()

    return render(request, 'blog/index.html', context)


