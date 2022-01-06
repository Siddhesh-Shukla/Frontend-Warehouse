from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'sign_up':
            signup_form = UserRegisterForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                messages.success(request, f'account created for {username}')
                return redirect('signup-signin')
        elif request.POST.get('submit') == 'sign_in':
            signin_form = AuthenticationForm(request, data=request.POST)
            if signin_form.is_valid():
                username = signin_form.cleaned_data.get('username')
                password = signin_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("home")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            signup_form = UserRegisterForm()
            signin_form = AuthenticationForm()
    else:    
        signup_form = UserRegisterForm()
        signin_form = AuthenticationForm()
    return render(request, 'users/register.html', {'signup_form': signup_form, 'signin_form': signin_form})
    # if request.method == "POST":
        # if request.POST.get('submit') == 'sign_in':
        #     signin_form = AuthenticationForm(request, data=request.POST)
        #     if signin_form.is_valid():
        #         username = signin_form.cleaned_data.get('username')
        #         password = signin_form.cleaned_data.get('password')
        #         user = authenticate(username=username, password=password)
        #         if user is not None:
        #             login(request, user)
        #             messages.info(request, f"You are now logged in as {username}.")
        #             return redirect("home")
        #         else:
        #             messages.error(request,"Invalid username or password.")
        #     else:
        #         messages.error(request,"Invalid username or password.")
        # elif request.POST.get('submit') == 'sign_up':
    #     signup_form = UserRegisterForm(request.POST)
    #     if signup_form.is_valid():
    #         signup_form.save()
    #         username = signup_form.cleaned_data.get('username')
    #         messages.success(request, f'account created for {username}')
    #         return redirect('/')
    #     else:    
    #         signup_form = UserRegisterForm()
    # signup_form = UserRegisterForm()
    # return render(request, template_name="users/register.html", context={"signup_form":signup_form})
    # else:
    #     signin_form = AuthenticationForm()
    #     signup_form = UserRegisterForm()
    # return render(request, template_name="users/register.html", context={"signin_form":signin_form, "signup_form":signup_form})



@login_required
def profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm (request.POST, 
    #                                 request.FILES, 
    #                                 instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, "Your account has been updated")
    #         return redirect('profile')

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }

    # return render(request, 'users/profile.html', context)
    return render(request, 'users/profile.html')