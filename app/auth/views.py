from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required,current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''将login页面改成了部门介绍，所以没有数据读入了'''
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
                    sex=form.sex.data,
                    Class=form.Class.data,
                    favor=form.favor.data,
                    adjust=form.adjust.data,
                    like=form.like.data,
                    practice=form.practice.data,
                    yourself=form.yourself.data,
                    qq=form.qq.data,
                    phonenum=form.phonenum.data,
                    email=form.email.data,
                    username=form.username.data,)
        db.session.add(user)    #将表单添加至数据库
        db.session.commit()
        flash('报名成功！\n')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
