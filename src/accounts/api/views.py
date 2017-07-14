from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)


from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from rest_framework.filters import(
	SearchFilter,
	OrderingFilter,
	)

from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import (
	UserCreateSerializer
	)


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
