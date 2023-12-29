from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html', {
        'data': "This is main page content",
    })