from django.forms import ModelForm
from .models import Post

# 에러 메시지도 싸이월드 감성으로
ERROR_MESSAGES = {
    'name': {'required': '이름을 입력해주세요 -_-;;'},
    'content': {'required': '내용을 입력해주세요 -_-;;'},
}

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'minimi', 'is_secret']
        error_messages = ERROR_MESSAGES

class PostEditForm(ModelForm): # 수정할 때는 비밀 여부 빼고
    class Meta:
        model = Post
        fields = ['name', 'content', 'minimi']
        error_messages = ERROR_MESSAGES
