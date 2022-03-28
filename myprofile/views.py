from django.http import HttpResponse 
from django.template import loader 
from django.shortcuts import render #追加

# 変更
def top(request):
    context = {
       'name':'たろう',
    }

    return render(request, 'myprofile/top.html', context)
    return HttpResponse(html) 

def resume(request):
    return HttpResponse('職務経歴ページ!!')

