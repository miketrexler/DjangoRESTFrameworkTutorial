from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

# We're building our view using GenericAPIView, 
# and adding in ListModelMixin and CreateModelMixin.
#
# The base class provides the core functionality, 
# and the mixin classes provide the .list() and .create() actions. 
# We're then explicitly binding the get and post methods to the appropriate actions.
class SnippetList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

# Again we're using the GenericAPIView class to provide the core functionality, 
# and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.
class SnippetDetail(mixins.RetreiveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
