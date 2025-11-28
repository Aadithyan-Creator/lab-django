# profile/views.py
from django.shortcuts import render, get_object_or_404
from .models import Profile
from main.models import User

def profile_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = Profile.objects.filter(user=user).first() 
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'profile_detail.html', context)

def profile_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        phone = request.POST.get('phone_number')
        profile_pic = request.FILES.get('profile_picture')

        profile, created = Profile.objects.get_or_create(user=user)
        profile.bio = bio
        profile.phone_number = phone
        if profile_pic:
            profile.profile_picture = profile_pic
        profile.save()

        return render(request, 'success.html')

    return render(request, 'profile_form.html', {'user': user})
