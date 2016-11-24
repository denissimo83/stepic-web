from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, question_list, question_detail, popular_questions, question_add, answer_add
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', question_list),
    url(r'^login/', login),
    url(r'^signup/', signup),
    url(r'^question/(?P<id>\d+)/$', question_detail),
    url(r'^ask/', question_add),
    url(r'^popular/$', popular_questions),
    url(r'^new/', test),
    url(r'^answer/$', answer_add),
)
