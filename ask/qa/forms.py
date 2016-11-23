from django import forms

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not (title or len(title) > 0):
            raise forms.ValidationError(u'Название не может быть пустым')
        return title


    def clean_text(self):
        text = self.cleaned_data['text']
        if not (text or len(text) > 0):
            raise forms.ValidationError(u'Вопрос не может быть пустым')
        return text


    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question



class AnswerForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.Textarea)

    def clean_question(self):
        question = self.cleaned_data['question']
        if not (question or question > 0):
            raise forms.ValidationError(u'Вопрос не существует')
        return question


    def clean_text(self):
        text = self.cleaned_data['text']
        if not (text or len(text) > 0):
            raise forms.ValidationError(u'Ответ не может быть пустым')
        return text


    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

