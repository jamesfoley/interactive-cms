from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.generic import FormView, View

from ..forms.auth import LoginForm


class Login(FormView):
    form_class = LoginForm
    template_name = 'manage/auth/login.html'
    success_url = '/manage/'

    def get_success_url(self):

        # Check to see if we have a next var in the GET vars
        next = self.request.GET.get('next', None)

        # If next, return it, else default success
        return next if next is not None else self.success_url

    def form_valid(self, form):

        # Form is valid, log the user in
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        login(self.request, user)

        return super(Login, self).form_valid(form)


class Logout(View):

    # Get request
    def get(self, request, *args, **kwargs):

        # Pragmatically log user out
        logout(request)

        # Take user to manage login page
        return redirect('manage:login')


