from django.shortcuts import render

# Create your views here.
def user_profile_view(request):
    return render(request, 'user_profile.html', {
        'data': "This is user profile content",
    })