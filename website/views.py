# Storing standard roots for the website
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import DiaryEntry, User
from . import db, login_manager
import json

views = Blueprint('views', __name__)
    
# this is the front page that the user will see when they aren't logged in
@views.route('/')
def home():
    active_page = 'home'
    if current_user.is_authenticated:
        first_name = current_user.first_name
        return render_template('home.html', first_name=first_name, active_page=active_page)
    
    return render_template('front-page.html')

@views.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    active_page = 'blog'
    return render_template('blog.html', entries=DiaryEntry.query.all(), user=User.query.all(), active_page=active_page)

@views.route('/diary_entry', methods=['GET', 'POST'])
@login_required
def diary_entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            flash('Title and content are required', category='error')
        else:
            entry = DiaryEntry(
            title = title,
            content = content,
            user = current_user,
            )
            db.session.add(entry)
            db.session.commit()
            flash('New entry to your diary was created', category='success')
            return redirect(url_for('views.blog'))
    
    return render_template('create.html', user=current_user)

@views.route('/entry/<int:entry_id>')
def entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    return render_template('entry.html', entry=entry)

@views.route("/edit/<int:entry_id>", methods=["GET"])
@login_required
def edit_page(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)

    return render_template("edit.html", entry=entry)

@views.route('/edit/<int:entry_id>', methods=['POST'])
@login_required
def edit_entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)

    if 'title' in request.form:
        entry.title = request.form['title']
    
    if 'content' in request.form:
        entry.content = request.form['content']

    db.session.commit()
    return redirect(url_for('views.entry', entry_id=entry.id))

@views.route('/delete/<int:entry_id>', methods=['GET'])
@login_required
def delete_entry(entry_id):
    entry = DiaryEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('views.blog'))
