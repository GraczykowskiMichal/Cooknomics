from django.http import HttpResponse


def news_list(request):
    return HttpResponse("News:")


def article(request, article_slug):
    return HttpResponse("News:")