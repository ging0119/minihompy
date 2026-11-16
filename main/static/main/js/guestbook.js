// csrf 토큰은 base.html의 meta 태그에서 꺼내 씀
function getCsrfToken() {
  return document.querySelector('meta[name="csrf-token"]').content;
}

// 비밀로 하기 / 공개로 하기
function toggleSecret(url, value) {
  fetch(url, {
    method: 'PATCH',
    headers: {
      'X-CSRFToken': getCsrfToken(),
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'is_secret=' + value
  }).then(r => {
    if (!r.ok) throw new Error('바꾸기 실패 ㅠ_ㅠ');
    location.reload();
  }).catch(e => alert(e.message));
}

// 삭제
function deletePost(url, nextUrl) {
  if (!confirm('정말 지울꺼임?? ㅠ_ㅠ')) return;
  fetch(url, {
    method: 'DELETE',
    headers: {'X-CSRFToken': getCsrfToken()}
  }).then(r => {
    if (!r.ok) throw new Error('삭제 실패 ㅠ_ㅠ');
    location.href = nextUrl;
  }).catch(e => alert(e.message));
}

// 수정 페이지 (forms.html)
const editForm = document.getElementById('edit-form');
if (editForm) {
  editForm.addEventListener('submit', e => {
    e.preventDefault();
    fetch(editForm.dataset.url, {
      method: 'PATCH',
      headers: {
        'X-CSRFToken': getCsrfToken(),
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams(new FormData(editForm))
    }).then(r => r.json().then(data => {
      if (r.ok) {
        location.href = editForm.dataset.url;
        return;
      }
      if (data.error) {
        alert(data.error);
        return;
      }
      // 에러 메시지를 폼 위에 보여주기
      const box = document.getElementById('errors');
      box.innerHTML = '';
      for (const field in data.errors) {
        data.errors[field].forEach(msg => {
          const li = document.createElement('li');
          li.textContent = '※ ' + msg;
          box.appendChild(li);
        });
      }
    })).catch(() => alert('수정 실패 ㅠ_ㅠ'));
  });
}

// 창 크기에 맞춰 미니홈피를 키우기 (비율은 그대로)
function fitHompy() {
  const ie = document.querySelector('.ie');
  ie.style.zoom = 1;
  const zoomW = (window.innerWidth - 20) / ie.offsetWidth;
  const zoomH = (window.innerHeight - 20) / ie.offsetHeight;
  ie.style.zoom = Math.min(zoomW, zoomH);
}
fitHompy(); // 화면 뜨자마자 바로 맞춤
window.addEventListener('resize', fitHompy);
