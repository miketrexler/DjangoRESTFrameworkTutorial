from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Generic Class Based Views
class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
