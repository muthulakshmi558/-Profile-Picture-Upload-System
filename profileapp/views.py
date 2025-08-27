from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile


def home(request):
    """Homepage: show all uploaded profiles."""
    profiles = UserProfile.objects.all().order_by('-created_at')
    return render(request, 'profileapp/home.html', {'profiles': profiles})


def create_profile(request):
    """Upload a new profile with image."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = UserProfileForm()
    return render(request, 'profileapp/profile_form.html', {'form': form})


def profile_detail(request, pk):
    """View a single profile detail page."""
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'profileapp/profile_detail.html', {'profile': profile})
