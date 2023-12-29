from django.shortcuts import render

# Create your views here.
def search_result_view(request):
    return render(request, 'search_result.html', {
        'data': "This is the search result ",
    })
