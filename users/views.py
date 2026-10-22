from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm, UserProfileForm
from django.core.mail import send_mail

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        email = form.cleaned_data.get('email')
        subject = 'Добро пожаловать!'
        message = f'Здравствуйте, {self.object.username}!\n\nСпасибо за регистрацию на нашем сайте.'
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [email], fail_silently=False)
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_edit.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user