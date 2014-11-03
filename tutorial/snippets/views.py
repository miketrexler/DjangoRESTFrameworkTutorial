from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework import viewsets

#ViewSet
class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		#'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})