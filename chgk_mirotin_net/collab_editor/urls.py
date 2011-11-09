from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('collab_editor.views',
    ('^/$', 'index')
)
