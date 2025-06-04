from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def profilePage(request):
    return render(request, 'account/profilePage.html', {'section': 'profile'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileEditForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Create the user
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Create the profile with the cleaned data
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileEditForm()
        
    return render(request, 'account/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

    
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})