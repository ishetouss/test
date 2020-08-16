from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from django.http import HttpResponseRedirect
# Create your models here.

# register_view

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = '/'
    
    extra_context = {
        'title': 'Register'
    }    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
    
    def get_success_url(self):
        return self.success_url
    
    def post(self, request, *args, **kwargs):
        if User.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, "this email is already takes")
            return redirect('register')
        
        user_form =UserRegistrationForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            print(user_form.errors)
            return render(request, 'register.html', {'form': user_form} )
            
class LoginView(FormView):
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'login.html'

    extra_context = {
        'title': 'Login'
    }
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)












# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for {username}")
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)