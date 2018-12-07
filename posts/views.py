from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm


def post_view(request):
    qs = Post.objects.all()
    return render(request, 'posts/home.html', {'objects_list': qs})


def set_like(request, pk):
    post_qs = Post.objects.filter(pk=pk)
    
    if request.user.is_authenticated:
        is_liked = Post.objects.like_toggle(request.user, post_qs.first())
    return redirect('home')


def set_unlike(request, pk):
    post_qs = Post.objects.filter(pk=pk)
    if request.user.is_authenticated:
        is_liked = Post.objects.unlike_toggle(request.user, post_qs.first())
    return redirect('home')
    
    
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('home')
    success_message = "The post was created!"
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(PostCreateView, self).form_valid(form)
