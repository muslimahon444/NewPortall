from django.shortcuts import render, get_object_or_404,redirect
from .models import NewArticle, Category
from .forms import NewsArticleForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    if query := request.GET.get('q'):
        news = NewArticle.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        news = NewArticle.objects.all()
        
    categories = Category.objects.all()
    news = NewArticle.objects.all()
    context = {
    
        'categories': categories,
        
        'news': news,
    }
    return render(request, 'new/home.html', context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    news_list = NewArticle.objects.filter(category=category)
    

    context = {
        'category': category,
        'categories': categories,
        
        'news_list': news_list,

    }
    return render(request, 'new/category.html', context)

def create_news(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)  # Получаем объект, но не сохраняем в БД
            news.author = request.user      # Устанавливаем автора
            news.save()  
            return redirect('new:home')
    else:
        form = NewsArticleForm()

    
    return render(request, 'new/create_news.html', {'form': form})

class NewsUpdateView(UpdateView):
    model = NewArticle
    form_class = NewsArticleForm
    template_name = 'new/update.html'
    success_url = reverse_lazy('new:home')




class NewsDeleteView(DeleteView):
    model = NewArticle 
    template_name = 'new/delete_news.html'
    context_object_name = 'new'
    success_url = reverse_lazy('new:home')

def news_delete_view(request, pk):
    new = NewArticle.objects.get(pk=pk)
    new.delete()
    return redirect('new:home')
    
def news_detail_view(request, pk):
    new = get_object_or_404(NewArticle, pk=pk)
    news_list = NewArticle.objects.filter(category=new.category).exclude(pk=new.pk)
    categories = Category.objects.all()

    
    
    categories = Category.objects.all()
    context = {
        'new': new,
        'categories': categories,
        'news_list': news_list,
    }
    return render(request, 'new/detail.html', context)



    
