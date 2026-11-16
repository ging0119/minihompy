# 깅이의 미니홈피

장고 게시판 과제입니다. 싸이월드 미니홈피 방명록처럼 꾸며 봤습니다.

사이트: https://gayoung0119.pythonanywhere.com

## 실행 방법

```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample
python manage.py runserver
```

loaddata는 예시 방명록을 넣는 거라 안 해도 됩니다.

## 기능

방명록 목록, 글쓰기, 상세보기, 수정, 삭제, 비밀글이 있습니다.

목록이랑 글쓰기는 함수형 뷰(index, create_post)로, 글 하나 보기/수정/삭제는 예제처럼 Article 클래스형 뷰로 만들었습니다.
form으로는 PATCH, DELETE를 보낼 수 없어서 수정이랑 삭제는 fetch로 요청했습니다.
PATCH는 request.POST에 값이 안 들어와서 request.body를 QueryDict로 읽었습니다.
