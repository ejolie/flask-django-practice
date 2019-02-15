from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3 as lite
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return redirect('/articles')
    
# 글 목록 페이지
@app.route('/articles') 
def articles():
    data = query('select_all', 'articles')
    return render_template('articles.html', data = data)
    
# 새 글 생성 Form
@app.route('/articles/new')
def new():
    return render_template('new.html')
    
# 새 글 생성
@app.route('/articles/create', methods=['POST']) 
def create():
    # Timezone
    KST = datetime.now(timezone('Asia/Seoul'))
    date_str = KST.strftime('%Y/%m/%d %H:%M')
    if request.method == 'POST':
        result = request.form
    params =  {
        'title': result.get('title'),
        'content': result.get('content'),
        'created_at': date_str,
        'author': result.get('author')
    }
    query('insert', 'articles', **params)
    return redirect('/articles')
    
# 글 상세 페이지
@app.route('/articles/<int:article_id>')
def article_detail(article_id):
    params = { 'id': article_id }
    data = query('select_id', 'articles', **params)
    return render_template('detail.html', data=data)
    
# 글 수정 Form
@app.route('/articles/<int:article_id>/edit') 
def article_edit(article_id):
    params = { 'id': article_id }
    data = query('select_id', 'articles', **params)
    return render_template('edit.html', data=data)

# 글 수정
@app.route('/articles/<int:article_id>/update', methods=['POST']) 
def article_update(article_id):
    # Timezone
    KST = datetime.now(timezone('Asia/Seoul'))
    date_str = KST.strftime('%Y/%m/%d %H:%M')
    if request.method == 'POST':
        result = request.form
    params =  {
        'id': article_id,
        'title': result.get('title'),
        'content': result.get('content'),
        'created_at': date_str,
        'author': result.get('author')
    }
    query('update', 'articles', **params)
    return redirect('/articles')
    
# 글 삭제
@app.route('/articles/<int:article_id>/delete') 
def article_delete(article_id):
    params = { 'id': article_id }
    query('delete', 'articles', **params)
    return redirect('/articles')

# SQL
def query(query, table, **kwargs):
    db = lite.connect('blog.db')
    cur = db.cursor()
    data = None
    
    if query == 'select_all':
        sql = "SELECT * FROM {} ORDER BY id DESC".format(table)
        cur.execute(sql)
        data = cur.fetchall()
        
    elif query == 'select_id':
        sql = "SELECT * FROM {} WHERE id={}".format(table, kwargs['id'])
        cur.execute(sql)
        data = cur.fetchone()

    elif query == 'insert':
        sql = "INSERT INTO {} (title, content, created_at, author) VALUES ('{}','{}', '{}', '{}')".format(table, kwargs['title'], kwargs['content'], kwargs['created_at'], kwargs['author'])
        cur.execute(sql)
        db.commit()
        
    elif query == 'update':
        sql = "UPDATE {} SET title='{}', content='{}', created_at='{}', author='{}' WHERE id={}".format(table, kwargs['title'], kwargs['content'], kwargs['created_at'], kwargs['author'], kwargs['id'])
        cur.execute(sql)
        db.commit()
        
    elif query == 'delete':
        sql = "DELETE FROM {} WHERE id={}".format(table, kwargs['id'])
        cur.execute(sql)
        db.commit()

    db.close()
    return data
    
if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
