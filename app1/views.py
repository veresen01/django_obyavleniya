from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import PostForm
from django.urls import reverse_lazy

from app1.models import Post, Rubric


# def index(request):
#     return HttpResponse("Здесь будет выведен список объявлений.")
# def index(request):
#     s = 'Объявления\r\n\r\n\r\n'
#     for bb in Post.objects.order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')

# def index(request):
#     # bbs = Post.objects.order_by('-published')
#     bbs = Post.objects.all()
#     return render(request, 'app1/index.html', {'bbs': bbs})
def index(request):
    post = Post.objects.all()
    rubrics = Rubric.objects.all()
    context = {'post': post, 'rubrics': rubrics}
    return render(request, 'app1/index.html', context)


def rubric_post(request, rubric_id):
    post = Post.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'post': post, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'app1/rubric_post.html', context)


class PostCreateView(CreateView):
    template_name = 'app1/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
