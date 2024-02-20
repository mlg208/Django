import json

from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# from bboard.models import Bb, Rubric

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы вошли в систему')
            return redirect('testapp')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы успешно вышли из системы.')
    return redirect('index')  # Замените 'index' на URL вашей главной страницы



def index(request):
    resp_content = ('здесь будет', 'главная', 'страница', 'сайта')
    resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
    return resp

# def index_1(request):
#     file_name = r'static/bg.jpg'
#     return FileResponse(open(file_name, 'rb')
#                         , as_attachment=True,
#                         file_name='file.zip')
#
# def index(request):
#     data = {'title': 'мотоцикл', 'content': 'старый', 'price': 10000.0}
#     return JsonResponse(data, encoder=DjangoJSONEncoder)
#
# def index(request):
#     context = {'title': 'Тестовая страница 1'}
#     render(request, 'test.html', context) #template_name Это шаблон
#
# def index(request):
#     r = get_object_or_404( name='Транспорт')
#     return redirect(to='bboard:by_rubric', rubric_id=r.id)
#
# def index(request):
#     r = get_object_or_404( name='Транспорт')
#     bbs = get_list_or_404( rubric=r)
#     context = {'title': 'Тестовая страница ', 'bbs': bbs}
#     return render(request,'test.html', context)
#
# class IndexView(list_view):
#     model = Bb
#     template_name = 'index.html'
#     paginate_by = 2
#     context_object_name ='bbs'
#     paginator_orphans = 2
#
#     def get_queryset(self):
#         return Bb.objects.all()
#
#     def context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt_gt=0)
#         return context