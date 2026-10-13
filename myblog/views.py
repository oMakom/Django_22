from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'myblog/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'myblog/post_form.html'
    success_url = reverse_lazy('myblog:posts_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'myblog/post_form.html'
    success_url = reverse_lazy('myblog:posts_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'myblog/post_confirm_delete.html'
    success_url = reverse_lazy('myblog:posts_list')