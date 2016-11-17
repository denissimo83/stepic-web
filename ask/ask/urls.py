from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test, question_list, question_detail, popular_questions
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', question_list),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>\d+)/$', question_detail),
    url(r'^ask/', test),
    url(r'^popular/$', popular_questions),
    url(r'^new/', test),
)
