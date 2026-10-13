from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from config import settings
from .models import Post


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'myblog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1

        if self.object.views_count == 100:
            send_mail(
                subject='Поздравляем! Ваш пост достиг 100 просмотров!',
                message=f'Пост "{self.object.title}" набрал 100 просмотров.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

        self.object.save()
        return self.object


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