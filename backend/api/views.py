from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Review


class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # pega as reviews de um usuario
        user = self.request.user
        return Review.objects.filter(author=user)
    
    def perform_create(self, serializer): # cria review
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class ReviewDelete(generics.DestroyAPIView): # deleta review se o usuario estiver autenticado
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
