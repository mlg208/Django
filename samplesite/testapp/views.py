import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from samplesite.bboard.models import Rubric, Bb


# def index(request):
#     resp_content = ('здесь будет', 'главная', 'страница', 'сайта')
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
#     return resp

# def index(request):
#     file_name = r'static/bg.jpg'
#     return FileResponse(open(file_name, 'rb')
#                         , as_attachment=True,
#                         file_name='file.zip')

# def index(request):
#     data = {'title': 'мотоцикл', 'content': 'старый', 'price': 10000.0}
#     return JsonResponse(data, encoder=DjangoJSONEncoder)

# def index(request):
#     context = {'title': 'Тестовая страница 1'}
#     render(request, template_name='test.html', context) #template_name Это шаблон

# def index(request):
#     r = get_object_or_404(Rubric, name='Транспорт')
#     return redirect(to='bboard:by_rubric', rubric_id=r.id)

# def index(request):
#     r = get_object_or_404(Rubric, name='Транспорт')
#     bbs = get_list_or_404(Bb, rubric=r)
#     context = {'title': 'Тестовая страница ', 'bbs': bbs}
#     return render(request,template_name= 'test.html', context)