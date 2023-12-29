from django.shortcuts import render, redirect


# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html', {
        'data': "Welcome to book rating searching website!",
    })

