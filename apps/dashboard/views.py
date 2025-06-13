from django.shortcuts import render
from .models import Post
# Create your views here.
# def index(request):
#     return render(request, 'dashboard/index.html')


def show(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'dashboard/show.html', context)

def insert(request):
    if request.method == 'POST':
        image_ = request.FILES['post_image']
        title_ = request.POST['title']
        content_ = request.POST['content']

        new_post = Post.objects.create(
            image = image_,
            title = title_,
            content = content_
        )
        new_post.save()

    return render(request, 'dashboard/insert.html')