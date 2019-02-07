# Mini : 블로그 만들기
## 1. 데이터 베이스
```sql
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT,
    author TEXT NOT NULL
);
```

&nbsp;

## 2. 페이지
### 1. 글 목록
![글 목록](./screenshots/1-articles.PNG)


&nbsp;

### 2. 새 글 생성 Form
![새 글 생성 Form](./screenshots/2-new.PNG)


&nbsp;

### 3. 새 글 생성 


&nbsp;

### 4. 글 상세 페이지
![글 상세 페이지](./screenshots/3-article-detail.PNG)


&nbsp;

### 5. 글 수정 Form
![글 수정 Form](./screenshots/4-article-edit.PNG)


&nbsp;

### 6. 글 수정


&nbsp;

### 7. 글 삭제