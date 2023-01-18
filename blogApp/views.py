from django.shortcuts import render
from django.views import generic
from .models import BlogModel
# Create your views here.


class AllBlogsView(generic.ListView):
    queryset = BlogModel.objects.order_by('-created')
    context_object_name = 'blogs'
    template_name = 'blog_list.html'
    class Meta:
        order_by = ['-created']
