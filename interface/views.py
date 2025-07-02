from django.shortcuts import render, redirect 
from django.urls import reverse
from infrastructure.repositories import  CategoryRepository, PostRepository, PostCreateRepository
from interface.models import User, Category, Post 
from application.use_case import CategoryUseCase, PostUseCase , PostCreateUseCase , PostUpdateUseCase
from. forms import PostForm
# Create your views here.

def index(request):
    category_repository = CategoryRepository()
    post_repository = PostRepository()  
    category_use_case = CategoryUseCase(category_repository)
    post_use_case = PostUseCase(post_repository)
    categories = category_use_case.get_all_categories()
    posts = post_use_case.get_all_posts()   
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'interface/index.html' , context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Remplacer 'category' (instance Category) par 'category_id'
            data['category_id'] = data['category'].id
            del data['category']

            postRepo = PostCreateRepository()
            posusercase = PostCreateUseCase(postRepo)
            posusercase.create_post(**data, user_id=request.user.id)

            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'interface/post_create.html', {'form': form})


def update_post(request, post_id):
    postRepo = PostRepository()
    postUseCase = PostUseCase(postRepo)
    post = postUseCase.get_post_by_id(post_id)

    if not post:
        return redirect('index')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            data = form.cleaned_data
            data['category_id'] = data['category'].id
            del data['category']

            postUpdateUseCase = PostUpdateUseCase(postRepo)
            postUpdateUseCase.update_post(post_id, **data, user_id=request.user.id)

            return redirect('index')
    else:
        form = PostForm(instance=post)

    return render(request, 'interface/post_update.html', {'form': form, 'post': post})



def delete_post(request, post_id):
    postRepo = PostRepository()
    postUseCase = PostUseCase(postRepo)
    post = postUseCase.get_post_by_id(post_id)
    postRepo.delete_post(post_id)
    return redirect('index')