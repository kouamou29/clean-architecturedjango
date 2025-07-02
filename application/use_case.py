from domain.entiers import EntierCategory, EntiersPost
from interface.models import Category, Post


class CategoryUseCase:
    def __init__(self, category_repository):
        self.category_repository = category_repository

    def get_all_categories(self):
        categories = self.category_repository.get_all_categories()
        return [EntierCategory(name=category.name) for category in categories]

    def get_category_by_id(self, category_id):
        category = self.category_repository.get_category_by_id(category_id)
        if category:
            return EntierCategory(name=category.name)
        return None
    
class PostUseCase:
    def __init__(self, post_repository):
        self.post_repository = post_repository

    def get_all_posts(self):
        posts = self.post_repository.get_all_posts()
        return [EntiersPost(id=post.id, title=post.title, content=post.content,user_id=post.user.id,category_id=post.category.id,created_at=post.created_at) for post in posts]

    def get_post_by_id(self, post_id):
        post = self.post_repository.get_post_by_id(post_id)
        return post if post else None
    
class PostCreateUseCase:
    def __init__(self, post_create_repository):
        self.post_create_repository = post_create_repository

    def create_post(self, title, content, user_id, category_id):
        post = self.post_create_repository.create_post(
    
            title=title,
            content=content,
            user_id=user_id,
            category_id=category_id
        )
        if post:
            return EntiersPost(
                id=post.id,
                title=post.title,
                content=post.content,
                user_id=post.user.id,
                category_id=post.category.id,
                created_at=post.created_at
            )
        return None


class PostUpdateUseCase:
    def __init__(self, post_repository):
        self.post_repository = post_repository

    def update_post(self, post_id, title, content, user_id, category_id):
        return self.post_repository.update_post(
            post_id=post_id,
            title=title,
            content=content,
            user_id=user_id,
            category_id=category_id
        )

class PostDeleteUseCase:
    def __init__(self, post_repository):
        self.post_repository = post_repository

    def delete_post(self, post_id):
        return self.post_repository.delete_post(post_id)