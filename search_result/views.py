from django.shortcuts import render
from .models import Books_rating,books_data,Books,Ratings,Users
from django.db.models import F,Q
# Create your views here.
from django.db.models import Avg,Min,Max,Count

def search_result_view(request):
    if request.method == "POST":
        search_key = request.POST.get('searchKey', '')
        # 使用 annotate 計算每個標題的平均評分
        Rating_full = Books_rating.objects.select_related('Title')
        search_results = (
            Rating_full
            .filter(Title__Title__icontains=search_key)
            .values('Title__Title')
            .annotate(avg_score=Avg('review_score'),
                      rating_count = Count('Title__Title'),
                      categories = F('Title__categories'),
                      description = F('Title__description'),
                      min_price=Min('Price'),
                      max_price=Max('Price'),
                      authors=F('Title__authors'),  # 獲取作者信息
                      publisher=F('Title__publisher'),  # 獲取出版商信息
                      publishedDate=F('Title__publishedDate'))  # 獲取出版日期信息
            .order_by('-avg_score')  # 按 review_score 遞減排序
        )
        Rating_full2 = Ratings.objects.select_related('ISBN','User_ID')
        search_results2=(
            Rating_full2
            .filter(Q(ISBN__Book_Title__icontains=search_key ) | Q(ISBN__ISBN__icontains=search_key))
            .values('ISBN__ISBN')
            .annotate(avg_score=Avg('Book_Rating'),
                      rating_count = Count('ISBN__ISBN'),
                      Title = F('ISBN__Book_Title'),
                      author = F('ISBN__Book_Author'),
                      publisher = F('ISBN__Publisher'),
                      Year_Of_Publication = Min('ISBN__Year_Of_Publication')
                      )
            .order_by('-avg_score')
        )
        # 將搜尋結果和詳細信息結合
        return render(request, 'search_result.html', {
            'data': "以下是搜尋關鍵字：" + request.POST.get('searchKey') + " 的結果",
            'context': search_results,
            'context2': search_results2
        })
    else:
        return render(request, 'search_result.html')
