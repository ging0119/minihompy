from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm, PostEditForm
from .models import Post
from django.http import HttpResponseNotAllowed, JsonResponse, QueryDict

def index(request):
    return render(request,
                'main/boards.html',
                context={
                    'posts':Post.objects.all(),
                    'form':PostForm(),
                })

def create_post(request): #function-based view
    if request.method == "GET":
        # 글쓰기 칸이 목록 페이지에 있어서 목록으로 보냄
        return redirect('index')
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        # 에러는 글쓰기 칸 위에 보여줌
        return render(request,
                    'main/boards.html',
                    context={
                        'posts':Post.objects.all(),
                        'form':form,
                    },
                    status=400)
    else: #delete, put, etc.
        return HttpResponseNotAllowed(["GET", "POST"])

def edit_post(request, pk): #수정 페이지
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    post = Post.objects.filter(idx=pk).first()
    if post is None:
        return render(request, 'main/articles.html', {"post":None}, status=404)
    return render(request, 'main/forms.html', {"post":post, "form":PostEditForm(instance=post)})

class Article(View): #class-based view
    def get(self, request, pk):
        post = Post.objects.filter(idx=pk).first()
        if post is None:
            return render(request, 'main/articles.html', {"post":None}, status=404)
        return render(request, 'main/articles.html', {"post":post})

    def post(self, request, pk):
        # create_post와 동일한 기능으로 연결
        return create_post(request)

    def patch(self, request, pk):
        post = Post.objects.filter(idx=pk).first()
        if post is None:
            return JsonResponse({'error':'없는 방명록이에요 OTL'}, status=404)
        # PATCH는 request.POST가 비어있어서 body를 직접 읽음
        data = QueryDict(request.body)

        # 비밀로 하기 / 공개로 하기
        if 'is_secret' in data:
            post.is_secret = data['is_secret'] == 'true'
            post.save(update_fields=['is_secret'])
            return JsonResponse({'ok':True})

        # 이름, 내용, 미니미 수정
        form = PostEditForm(data, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save(update_fields=['name', 'content', 'minimi'])
            return JsonResponse({'ok':True})
        return JsonResponse({'errors':form.errors}, status=400)

    def delete(self, request, pk):
        post = Post.objects.filter(idx=pk).first()
        if post is None:
            return JsonResponse({'error':'없는 방명록이에요 OTL'}, status=404)
        post.delete()
        return JsonResponse({'ok':True})
