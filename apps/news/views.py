from rest_framework import generics
from .models import Types, News
from .serializers import NewsUpdateSerializer, TypeListSerializer, NewsListSerializer, TypeCreateSerializer, NewsUpdateSerializer, TypeUpdateSerializer, NewsDeleteSerializer, NewsCreateSerializer, TypeDeleteSerializer

class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        type = self.request.query_params.get('type')
        if type is not None:
            queryset = queryset.filter(type = type)
        return queryset

class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

class NewsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer

class NewsDeleteView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDeleteSerializer

class TypeListView(generics.ListAPIView):
    queryset = Types.objects.all()
    serializer_class = TypeListSerializer

class TypeCreateView(generics.CreateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypeCreateSerializer

class TypeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypeUpdateSerializer

class TypeDeleteView(generics.DestroyAPIView):
    queryset = Types.objects.all()
    serializer_class = TypeDeleteSerializer