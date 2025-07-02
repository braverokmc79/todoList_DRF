// 목록과 상세에서 공통 사용 가능한 기능 모듈화


// 좋아요 토글
function toggleLike(id) {
  axiosInstance.post(`/api/interaction/likes/${id}/toggle/`)
    .then(res => {
      const { is_liked, like_count } = res.data;
      const btn = document.querySelector(`.likeBtn[data-id="${id}"]`);
      if (btn) btn.innerHTML = `${is_liked ? '💔' : '❤️'} <span class="count">${like_count}</span>`;
    })
    .catch(err => console.error("좋아요 토글 실패:", err));
}

// 북마크 토글
function toggleBookmark(id) {
  axiosInstance.post(`/api/interaction/bookmarks/${id}/toggle/`)
    .then(res => {
      const { is_bookmarked, bookmark_count } = res.data;
      const btn = document.querySelector(`.bookmarkBtn[data-bookmark-id="${id}"]`);
      if (btn) btn.innerHTML = `🔖 <span class="count">${bookmark_count}</span>`;
    })
    .catch(err => console.error('북마크 토글 실패:', err));
}

// 댓글 불러오기
function loadComments(todoId, listElement) {
  axiosInstance.get(`/api/interaction/comments/`, { params: { todo_pk: todoId } })
    .then(res => {
      const payload = Array.isArray(res.data) ? res.data : Array.isArray(res.data.results) ? res.data.results : (res.data.data || []);
      listElement.innerHTML = '';
      payload.forEach(c => {
        const li = document.createElement('li');
        li.innerHTML = `${c.user.username || c.username}: ${c.content} 
          <button class="comment-like-btn" data-id="${c.id}">👍 ${c.like_count}</button>`;
        li.querySelector('.comment-like-btn')?.addEventListener('click', e => {
          e.stopPropagation();
          toggleCommentLike(c.id);
        });
        listElement.appendChild(li);
      });
    })
    .catch(err => console.error('댓글 로드 실패:', err));
}

// 댓글 등록
function postComment(todoId, content, listElement) {
  if (!content) return alert("댓글을 입력하세요");

  axiosInstance.post("/api/interaction/comments/", { todo_pk: todoId, content: content })
    .then(() => {
      loadComments(todoId, listElement);

      const todoElement = listElement.closest('.todo-item');
      const countSpan = todoElement?.querySelector('.commentToggleBtn .count');
      if (countSpan) {
        const currentCount = parseInt(countSpan.textContent || '0', 10);
        countSpan.textContent = currentCount + 1;
      }
    })
    .catch(error => {
      console.error("댓글 등록 실패:", error.response?.data || error);
      alert("댓글 등록 실패:\n" + JSON.stringify(error.response?.data, null, 2));
    });
}

// 댓글 좋아요
function toggleCommentLike(commentId) {
  axiosInstance.post(`/api/interaction/commentlikes/${commentId}/toggle/`)
    .then(() => {
      const commentBtn = document.querySelector(`.comment-like-btn[data-id="${commentId}"]`);
      const todoElement = commentBtn.closest('.todo-item');
      const todoId = todoElement?.querySelector('.likeBtn')?.dataset?.id;
      const listElement = todoElement?.querySelector('.commentList');

      if (todoId && listElement) {
        loadComments(todoId, listElement);
      }
    })
    .catch(err => console.error("댓글 좋아요 실패:", err));
}
