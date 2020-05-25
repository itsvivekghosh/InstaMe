from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (ListView, CreateView, DeleteView, DetailView,
                                  UpdateView)
from PIL import Image
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from .forms import PostUpdateForm


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context={
        'posts': Post.objects.all()
    })


def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginated_by = 2


class PostDetailView(DetailView):
    model = Post


class CreateNewView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'Captions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.html'
    paginated_by = 2

    def get_queryset(
            self):  #checks the query request is currect or not (override)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        post = Post.objects.filter(author=user).order_by('-date_posted')
        return post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['Captions', 'image']

    def form_valid(
            self,
            form):  #used when we have to valid the user that is requesting the
        #form ie.jo user hai wo request kar rha h form ki usko update karo
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(
            self
    ):  #tests the user about the user updating the form is that user who is requesting and author the requested post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):

        post = self.get_object()
        if self.request.user == post.author:
            messages.warning(self.request,
                             f"The post will be deleted permanently")
            return True
        return False


@login_required
def UpdatePost(request):
    template_name = 'blog/post_detail.html'
    form = PostUpdateForm(request.POST or None,
                          request.FILES,
                          instance=request.user.profile)
    if request.method == 'POST':

        errors = None
        if form.is_valid():
            form.save()

            messages.success(request, f'Your Account has been updated')
            return render(request, template_name, form)
        if form.errors:
            errors = form.errors

        form = PostUpdateForm(instance=request.user.profile)
        context = {
            'form': form,
            "errors": errors,
        }
        return render(request, template_name, context)

    else:
        form = PostUpdateForm()
        return render(request, template_name, form)
