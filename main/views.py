from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ( 
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    if request.method =='GET':
        return render(request, 'main/index.html', context)
    elif request.is_ajax():
        data_entered = request.POST.get('text', None)
        if data_entered:
            response = {
                'msg': data_entered
            }
            return JsonResponse(response)
        else:
            response = {
                'msg': ""
            }
            return JsonResponse(response)

def workspace(request):
    # if request.method =='GET':
    return render(request, 'main/editPage.html')
    # elif request.is_ajax():
    #     data_entered = request.POST.get('text', None)
    #     if data_entered:
    #         response = {
    #             'msg': data_entered
    #         }
    #         return JsonResponse(response)
    #     else:
    #         response = {
    #             'msg': ""
    #         }
    #         return JsonResponse(response)

class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_post.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'html', 'css']
    template_name = 'main/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'html', 'css']
    template_name = 'main/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False