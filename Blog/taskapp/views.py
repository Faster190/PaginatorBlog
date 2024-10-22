from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.


def blog(request):
    posts = Post.objects.all().order_by("-created_at")
    print(request.GET)
    if request.GET.get("amount_of_posts"):
        number = int(request.GET.get("amount_of_posts"))
    else:
        number = 3
    paginator = Paginator(posts, number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(type(number))
    return render(request, "blog_template.html", {"page_obj": page_obj, "amount_of_posts": number,
                                                  "range": range(1, 5)})
