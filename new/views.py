from django.shortcuts import render, get_object_or_404,redirect
from .models import NewArticle, Category
from .forms import NewsArticleForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import logout


def home(request):
    # Получаем параметры фильтрации
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    # Базовый запрос (только опубликованные статьи)
    news_list = NewArticle.objects.filter(published=True).order_by('-created_at')
    
    # Применяем фильтры
    if search_query:
        news_list = news_list.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    if category_id:
        news_list = news_list.filter(category_id=category_id)
    
    # Пагинация
    paginator = Paginator(news_list, 5)  # 5 новостей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Получаем все категории
    categories = Category.objects.all()
    news = NewArticle.objects.all()
    
    context = {
        'page_obj': page_obj,  # Используем page_obj вместо news
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'news': news
    }
    return render(request, 'home.html', context)

def bod(request, pk=None):
    if pk:
        # Если pk передан, то это редактирование существующей статьи
        news = get_object_or_404(NewArticle, pk=pk)
    else:
        # Иначе создаем новую статью
        news = NewArticle()
    
    if request.method == 'POST':
        # Обработка формы
        form = NewsArticleForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsArticleForm(instance=news)
    
    categories = Category.objects.all()
    
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'bod.html', context)


def news_delete(request):
    return render(request, 'news_delete.html')

def logout_view(request):
    
    logout(request)  
    return redirect('home')



    
