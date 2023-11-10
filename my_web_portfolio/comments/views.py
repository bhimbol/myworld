from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def comments(request):
    comments_list = Comment.objects.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
    return render(request, 'comment.html', {'comments_list': comments_list, 'form': form})
