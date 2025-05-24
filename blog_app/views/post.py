from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog_app.forms import CommentForm
from blog_app.models import Post
from blog_app.tasks.email_tasks import send_welcome_email

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog_app/index.html"


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog_app/post_detail.html'


def post_detail(request, slug):
    # apply_async will runs the task on worker via redis ( enqueue task to redis)
    send_welcome_email.apply_async(("all user",))
    template_name = "blog_app/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
