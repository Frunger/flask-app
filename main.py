from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于会话管理


# 检查用户名是否存在于数据库中
def check_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user


# 添加新用户到数据库
def add_user_to_db(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def a():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return "用户名不能为空！"

        user = check_user(username)
        if user:
            session['username'] = username  # 存储用户名到会话
            return redirect(url_for('b'))
        else:
            return "用户不存在！"

    return render_template('a.html')


@app.route('/b')
def b():
    username = session.get('username')
    if not username:
        return redirect(url_for('a'))  # 如果没有登录，跳转回登录页
    return render_template('b.html', username=username)


# 添加新用户的路由
@app.route('/add_user/<username>')
def add_user(username):
    if not username:
        return "用户名不能为空！"

    user = check_user(username)
    if user:
        return f"用户 {username} 已经存在！"
    else:
        add_user_to_db(username)
        return f"用户 {username} 添加成功！"


if __name__ == '__main__':
    app.run(debug=False)
D
