from flask_login import UserMixin
from . import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    qq = db.Column(db.String(64), unique=True, index=True)
    phonenum = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    sex = db.Column(db.String(1), unique=True, index=True)
    #专业班级
    Class = db.Column(db.String(64), unique=True, index=True)
    #意愿部门
    favor = db.Column(db.String(64), unique=True, index=True)
    #是否接受调剂
    adjust = db.Column(db.String(1), unique=True, index=True)
    #喜爱
    like = db.Column(db.String(200), unique=True, index=True)
    #实践
    practice = db.Column(db.String(200), unique=True, index=True)
    #自评
    yourself = db.Column(db.String(200), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
