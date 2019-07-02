from flask import flash, redirect, render_template, session, url_for
from flask_login import login_required
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import Role, User, Place, Story

from . import main
from .forms import NameForm, RoleForm, EditUserForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', home=True)


@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

# @main.route('/login2')
# def login():
#     return render_template('auth/login.html') 

@main.route('/dicas')
@login_required
def dicas():
    return render_template('dicas.html')

@main.route('/relato/<int:id>')
def relato(id):
   story = Story.query.filter_by(id=id).first()
   story.content = story.content.replace('\n', '<br>')
   return render_template('relato.html', story=story)

@main.route('/MP')
@login_required
def mp():
    return render_template('mp.html')

@main.route('/Relatos')
@login_required
def relatos():
    places = Story.query.all()
    return render_template('relatos.html', places=places)

@main.route('/Galeria')
@login_required
def galeria():
    places = Place.query.all()
    return render_template('galeria.html', places=places)

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) 


@main.route('/user/list', methods=['GET', 'POST'])
def list_user():
    users = User.query.all()
    return render_template('list_user.html', users=users)


@main.route('/role/add', methods=['GET', 'POST'])
def add_role():
    form = RoleForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        new_role = Role()
        new_role.name = form.name.data
        db.session.add(new_role)
        db.session.commit()

        flash('Função cadastrada com sucesso.')
        return redirect(url_for('main.index'))
    return render_template('add_role.html', form=form, roles=roles)


@main.route('/edit-user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.filter_by(id=id).first()
    form = EditUserForm(user)
    return render_template('edit_user.html', form=form)