from django.shortcuts import render

# Create your views here.
def search_result_view(request):
    if request.method == "POST":
        mydata = ["this", "is", "where", "you", "put", "result", "in"] #mydata stores the result of query, use 'request.POST.get("searchKey")' to get keyword
        return render(request, 'search_result.html', {
        'data': "Below are searching result for: "+ request.POST.get('searchKey'), 
        'context': mydata,
    })