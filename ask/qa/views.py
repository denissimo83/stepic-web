from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from django.http import HttpResponseRedirect
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_detail(request, id):
    if request.method == 'POST':
        return answer_add(request, id)
    question = get_object_or_404(Question, id=id)
    form = AnswerForm(initial={'question':id,})
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': question.answer_set.all()[:],
        'form': form
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
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'popular_questions.html', {
        'questions': page.object_list,
        'page': page,
    })


def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html', {'form': form, })


def answer_add(request, id=2):
    if request.method == 'POST':
        #form = AnswerForm({'question_id': id, 'text': request.POST['text']})
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            question = answer.question
            url = question.get_absolute_url()
            #url = 'ask/'
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'answer_add.html', {
        'form': form,
         })
