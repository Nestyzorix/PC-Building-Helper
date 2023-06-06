from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView


class AboutMeView(TemplateView):
    template_name = 'myauth/about-me.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'myauth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')

    return render(request, 'myauth/login.html', {'error': 'Указаны неверные данные'})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))

