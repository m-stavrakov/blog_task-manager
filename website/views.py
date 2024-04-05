# Storing standard roots for the website
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import DiaryEntry, User, Tasks
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

@views.route('/calendar', methods=['GET'])
@login_required
def calendar():
    active_page = 'calendar'
    return render_template('calendar.html', active_page=active_page, tasks=Tasks.query.all())

@views.route('/calendar', methods=['POST'])
@login_required
def calendar_action():
    if request.method == 'POST':
        event_title = request.form['event-title']
        event_description = request.form['event-description']
        event_start = request.form['event-start-time']
        event_end = request.form['event-end-time']

        if not event_title or not event_description:
            flash('Title and description are required', category='error')
        else:
            task = Tasks(
            event_title = event_title,
            event_description = event_description,
            start_time = event_start,
            end_time = event_end,
            )
            db.session.add(task)
            db.session.commit()
            flash('New event to your calendar was created', category='success')
            return redirect(url_for('views.calendar'))

@views.route('/edit/<int:event_id>', methods=['GET'])
@login_required
def edit_tasks_page(event_id):
    event = Tasks.query.get_or_404(event_id)

    return render_template("edit_tasks.html", event=event)

@views.route('/edit/<int:event_id>', methods=['POST'])
@login_required
def edit_task(event_id):
    event = Tasks.query.get_or_404(event_id)

    if 'title' in request.form:
        event.title = request.form['event-title']
    
    if 'description' in request.form:
        event.description = request.form['event-description']

    db.session.commit()
    return redirect(url_for('views.calendar', event_id=event.id))

@views.route('/delete/<int:event_id>', methods=['POST'])
@login_required
def delete_task(event_id):
    event = Tasks.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('views.calendar'))