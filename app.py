from datetime import datetime
from flask import render_template, request, flash, redirect, url_for
from models import Posts
from settings import app, db


# @app.route("/")
# def home():
#
#     all_posts: list[Posts] = Posts.query.all()
#
#     print(type(all_posts))
#     print(all_posts)
#
#     return render_template("home.html", posts=all_posts)
#
#
@app.route("/post/<int:post_id>")
def show_post(post_id: int):

    post: Posts = db.get_or_404(Posts, post_id, description="Неверно указан ID поста")

    return render_template("show_post.html", post=post)
#
#
# @app.route("/create", methods=("GET", "POST"))
# def create_post():
#
#     if request.method == "POST":
#
#         title = request.form["title"]
#         content = request.form["text"]
#
#         if not title or not content:
#             flash("Необходимо указать заголовок и содержимое!")
#
#         else:
#             post = Posts(
#                 title=title,
#                 content=content,
#                 created=datetime.now()
#             )
#             db.session.add(post)  # Добавляем в таблицу
#             db.session.commit()  # Подтверждаем
#
#     return render_template("create_post.html")
#
#
# @app.route("/post/<int:post_id>/edit", methods=("GET", "POST"))
# def edit_post(post_id: int):
#
#     post: Posts = db.get_or_404(Posts, post_id, description="Неверно указан ID поста")
#
#     if request.method == "POST":
#
#         title = request.form["title"]
#         content = request.form["text"]
#
#         if not title or not content:
#             flash("Необходимо указать заголовок и содержимое!")
#
#
#         else:
#
#             post.title = title
#             post.content = content
#
#             db.session.add(post)
#             db.session.commit()
#
#             return redirect(url_for("show_post", post_id=post.id))
#
#     return render_template("edit_post.html", post=post)

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id: int):

    post: Posts = db.get_or_404(Posts, post_id, description="Неверно указан ID поста")
    if request.method == "GET":

        return render_template("show_post.html", post=post)

    else:
        db.session.delete(post)
        db.session.commit()

        return render_template("delete.html")


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run()