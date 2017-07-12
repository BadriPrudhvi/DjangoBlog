from rest_framework.serializers import ModelSerializer

from posts.models import Post

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
	class Meta:
		model = Post
		fields = [
		    "id",
			"title",
			"content",
			"image",
			"updated",
		]


class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"updated",
		]



