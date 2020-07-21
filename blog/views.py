from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
# Creating dummy data for the test only

# def home(request):
#     # return HttpResponse("This is your Home Blog page")

#     posts={'post':Post.objects.all()}
#     return render(request,'blog/home.html',posts)

def about(request):
    # return HttpResponse("This is your About Blog page")
    return render(request,'blog/about.html') 


class PostListView(ListView):
    model=Post
    template_name='blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name='post'
    ordering=['-date_posted']
    paginate_by=3
    

class PostDetailView(DetailView):
    model = Post
    #if we dont give the context_object_name in this class then default will ob 'object' which will used to called objects from model we created
    # if we dont give the template_name then default will be modelname_viewtype(https://docs.djangoproject.com/en/3.0/ref/class-based-views/).html or we can give our own template name 


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    template_name='blog/newblog.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    template_name='blog/newblog.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True;
        return False;


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='blog/delete.html'
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True;
        return False;