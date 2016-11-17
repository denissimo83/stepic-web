from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
#def test(request, *args, **kwargs):
#    return HttpResponse('OK')

def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'qa/question_detail.html', {
        'question': question,
        'answers': question.answer_set.all()[:]
        
        })


def question_list_all(request):
    question = Question.objects.filter(
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(question, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/question.html',
        'post': page.object_list,
        'paginator': paginator,
        'page': page,
    })



