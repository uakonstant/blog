from django.shortcuts import render

# Create your views here.  Create metod (def) с именем post_list, который принимает в request в качестве аргумента и return (возвращает) результат работы метода render, который соберет наш шаблон страницы blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})