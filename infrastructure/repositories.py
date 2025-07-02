from interface.models import  Category, Post
from django.shortcuts import get_object_or_404

class CategoryRepository:
    def get_all_categories(self):
        return Category.objects.all()
        
class PostRepository:
    def get_all_posts(self):
        return Post.objects.all()

    def get_post_by_id(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None 

    def get_posts_by_category(self, category_id):
        return Post.objects.filter(category_id=category_id)

    def get_posts_by_user(self, user_id):
        return Post.objects.filter(user_id=user_id)
    
    def update_post(self, post_id, title, content, user_id, category_id):
        try:
            post = Post.objects.get(id=post_id)
            post.title = title
            post.content = content
            post.user_id = user_id
            post.category_id = category_id
            post.save()
            return post
        except Post.DoesNotExist:
            return None
    
    
    def delete_post(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return True
        except Post.DoesNotExist:
            return False




class PostCreateRepository:
    def create_post(self, title, content, user_id, category_id):

      post = Post.objects.create(
          title=title,
          content=content,
          user_id=user_id,
          category_id=category_id
      )
      return post
  

        
   