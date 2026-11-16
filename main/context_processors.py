from .models import Post

# 사이드바, 게시판 위에 방명록 개수 보여주기
def guestbook(request):
    return {'guestbook_count': Post.objects.count()}
