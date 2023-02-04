from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, update_last_login
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_twitter_app import models


# Create your views here.


class HomeView(View):  # TODO контроллер класс
    template_name = 'django_twitter_app/home.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        # return HttpResponse(content=b"<h1>Hello World</h1>")
        # return JsonResponse(data={"response": 'res'}, safe=True)
        return render(request, 'django_twitter_app/home.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        context = {}
        # return HttpResponse(content=b"<h1>Hello World</h1>")
        # return JsonResponse(data={"response": 'res'}, safe=True)
        return render(request, 'django_twitter_app/home.html', context=context)


def home_view(request: HttpRequest) -> HttpResponse:  # TODO контроллер функция
    context = {}
    # return HttpResponse(content=b"<h1>Hello World</h1>")
    # return JsonResponse(data={"response": 'res'}, safe=True)
    return render(request, 'django_twitter_app/home.html', context=context)


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {}
        return render(request, 'django_twitter_app/register.html', context=context)
    elif request.method == "POST":

        # TODO получить с формы данные
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")

        if password1 and password1 != password2:
            raise Exception("пароли не совпадают!")
        if username and password1:
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=make_password(password1),
            )
            return redirect(reverse('django_twitter_app:login', args=()))  # name=
        else:
            raise Exception("данные не заполнены!")


def login_f(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {}
        return render(request, 'django_twitter_app/login.html', context=context)
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        if username and password:
            pass
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                context = {}
                login(request, user_obj)
                update_last_login(sender=None, user=user_obj)
                return redirect(reverse('django_twitter_app:home', args=()))
            else:
                raise Exception('данные не совпадают')
        else:
            raise Exception('no data')


def logout_f(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('django_twitter_app:login', args=()))


def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {}
        return render(request, 'django_twitter_app/post_create.html', context=context)
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        description = request.POST.get('description', "")
        models.Post.objects.create(
            user=request.user,
            title=title,
            description=description,
        )

        context = {}
        return redirect(reverse('django_twitter_app:post_list', args=()))


def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.all()
    context = {'posts': posts}
    return render(request, 'django_twitter_app/post_list.html', context=context)


def post_update(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'GET':
        post = models.Post.objects.get(id=pk)
        context = {'post': post}
        return render(request, 'django_twitter_app/post_update.html', context=context)
    elif request.method == 'POST':
        print('request:', request)
        title = request.POST.get('title', None)
        description = request.POST.get('description', "")
        post = models.Post.objects.get(id=pk)
        post.title = title
        post.description = description
        post.save()
        return redirect(reverse('django_twitter_app:post_detail', args=(pk,)))


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    comments = models.PostComment.objects.filter(article=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'django_twitter_app/post_detail.html', context=context)


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    post.delete()
    return redirect(reverse('django_twitter_app:post_list', args=()))


def post_pk_view(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'GET':
        # post_list = models.Post.objects.all()
        # print(f'post_list: {post_list}')
        # context = {'post_list': post_list}
        context = {}
        return render(request, 'django_twitter_app/post_detail.html', context=context)


def post_comment_create(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        text = request.POST.get('text', None)
        post = models.Post.objects.get(id=pk)
        models.PostComment.objects.create(
            user=request.user,
            article=post,
            text=text
        )

        return redirect(reverse('django_twitter_app:post_detail', args=(pk,)))


def post_comment_delete(request: HttpRequest, pk: int) -> HttpResponse:
    comment = models.PostComment.objects.get(id=pk)
    pk = comment.article.id
    comment.delete()
    return redirect(reverse('django_twitter_app:post_detail', args=(pk,)))


def homework_task(request: HttpRequest):
    list1 = [{'id': x, 'name': f'Emil  {x}', 'age': 10 + x} for x in range(1, 100)]
    return JsonResponse(data=list1, safe=False)
