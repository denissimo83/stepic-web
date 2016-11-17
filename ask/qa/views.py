from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': question.answer_set.all()[:],
        })



def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page



def question_list(request):
    questions = Question.objects.all()
    #paginator.baseurl = '/?page='
    page = paginate(request, questions)
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'page': page,
    })

def popular_questions(request):
    questions = Question.objects.all().popular
    page = paginate(request, questions)
    return render(request, 'popular_questions.html', {
        'questions': page.object_list,
        'page': page,
    })

