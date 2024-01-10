from django.shortcuts import render
from .models import Books_rating,books_data
from django.db.models import F
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
        
        # 從 books_data 中獲取每個標題的其他詳細信息
        title_details = Rating_full.filter(Title__Title__in=[result['Title__Title'] for result in search_results])
        
        # 創建一個字典將標題映射到其詳細信息
        title_details_dict = {title.Title: title for title in title_details}

        # 將搜尋結果和詳細信息結合
        search_results_with_details = [
            {
                'Title': result['Title__Title'],
                'avg_score': result['avg_score'],
                'details': title_details_dict.get(result['Title__Title'])
            }
            for result in search_results
        ]
        return render(request, 'search_result.html', {
            'data': "以下是搜尋關鍵字：" + request.POST.get('searchKey') + " 的結果",
            'context': search_results,
        })
    else:
        return render(request, 'search_result.html')
