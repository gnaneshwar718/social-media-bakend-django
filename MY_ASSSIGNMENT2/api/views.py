from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # Added import
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrieveView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostLikeView(APIView):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes += 1
        post.save()
        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)

class PostShareView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.shares += 1
        post.save()
        return Response({'message': 'Post shared successfully'}, status=status.HTTP_200_OK)



class PostCommentView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            comments = post.comments.split("\n")  # Assuming comments are separated by newline
            return Response({'comments': comments}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            # Read the request body as a string
            comment = request.body.decode('utf-8').strip()  # Remove leading/trailing whitespace
            if comment:
                # Append the comment on a new line
                post.comments += "\n" + comment
                post.save()
                return Response({'message': 'Comment added successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Comment field is required'}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

