from rest_framework.serializers import ModelSerializer

from posts.models import Post

from accounts.api.serializers import UserDetailSerializer

from rest_framework.serializers import(
		ModelSerializer,
		SerializerMethodField,
		HyperlinkedIdentityField
	)

class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    # "id",
			"title",
			"content",
			"image",
			"timestamp",
		]

class PostDetailSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
		    "id",
		    "user",
			"title",
			"content",
			"image",
			"updated",
		]


class PostListSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
			"user",
			"title",
			"content",
			"image",
			"updated",
		]



