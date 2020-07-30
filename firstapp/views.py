from django.shortcuts import render
from django.http import HttpResponse
#models 안에 Curriculum을 임포트한다.
from .models import Curriculum

def show(request):
    curriculum = Curriculum.objects.all()
    return render(request, 'show.html', {'list':curriculum})
    # html = ''
    # for c in curriculum:
    #     html += '%s번 %s<br>' % (c.id, c.name)
    # return HttpResponse( html )
    
def index1(request):
    return HttpResponse('index1')

def main(request):
    return HttpResponse('main!')

def main(request):
    return HttpResponse('main')


# Create your views here.
