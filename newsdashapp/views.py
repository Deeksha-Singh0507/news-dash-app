from django.shortcuts import render
from .scraper import fetch_news  # ✅ Correct filename used

def home(request):
    news_data = fetch_news()
    return render(request, 'newsdashapp/news_list.html', {'news_data': news_data})
