from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet
from rest_framework import renderers

# We're creating multiple views from each ViewSet class, 
# by binding the http methods to the required action for each view.
snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
	'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = patterns('snippets.views',
    url(r'^$', 'api_root'),

    url(r'^snippets/$', 
    	snippet_list, 
    	name='snippet-list'),

    url(r'^snippets/(?P<pk>[0-9]+)/$', 
    	snippet_detail,
    	name='snippet-detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', 
    	snippet_highlight,
    	name='snippet-highlight'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
