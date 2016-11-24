from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not (title or len(title) > 0):
            raise forms.ValidationError(u'Empty title')
        return title


    def clean_text(self):
        text = self.cleaned_data['text']
        if not (text or len(text) > 0):
            raise forms.ValidationError(u'Empty question')
        return text


    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question



class AnswerForm(forms.Form):
    question = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.Textarea)

#    def clean_question(self):
#        question = self.cleaned_data['question']
#        if not (question or question > 0):
#            raise forms.ValidationError(u'Question does no exist')
#        return question


#    def clean_text(self):
#        text = self.cleaned_data['text']
#        if not text:
#            raise forms.ValidationError(u'Empty question')
#        return text

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return answer

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=25)
	email = forms.EmailField()
	password = forms.CharField(max_length=20)

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User.objects.create_user(username, email, password)
		user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=25)

	def clean(self):
		return self.cleaned_data
	def save(self):
		user = authenticate(username, password)
		return user

