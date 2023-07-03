# from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 8
    # ordering = ['-id']

    # for more information go to https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))
    paginator = Paginator(category_posts.order_by('-post_date'), 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'categories.html', {'cat': cat.title().replace('-', ' '), 'category_posts': category_posts, 'page_obj': page_obj})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm  # make sure to include this if you want styling from bootstrap
    template_name = 'add_post.html'
    # fields = '__all__'

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddPostView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddCategoryView, self).get_context_data(
    #         *args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context


class UpdatePostView(UpdateView):
    model = Post
    # this form is the same as PostForm but it excludes the author field
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("home")

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(DeletePostView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context
