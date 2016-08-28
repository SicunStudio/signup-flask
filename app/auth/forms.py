from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    '''将login页面改成了部门介绍，所以没有数据读入了'''
    pass

class RegistrationForm(Form):
    qq = StringField('QQ',validators=[Required(),Length(1,64),Regexp('[0-9]')])
    phonenum = StringField('手机号',validators=[Required(),Length(1,64),Regexp('[0-9]')])
    email = StringField('邮箱', validators=[Required(), Length(1, 64)])
    username = StringField('姓名', validators=[Required(), Length(1, 64)])
    sex = StringField('性别',validators=[Required(),Length(1,50)])
    Class = StringField('班级',validators=[Required(),Length(1,64)])
    favor = StringField('意愿部门',validators=[Required(),Length(1,64)])
    adjust = StringField('是否接受调剂（输入 是/否）',validators=[Required(),Length(1,64)])
    like = TextField('爱好',validators=[Required(),Length(4,50)])
    practice = TextField('实践',validators=[Required(),Length(4,50)])
    yourself = TextField('个人评价',validators=[Required(),Length(4,50)])
    submit = SubmitField('报名')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

    def validate_qq(self, field):
        if User.query.filter_by(qq=field.data).first():
            raise ValidationError('qq already in use.')

    def validate_phonenum(self, field):
        if User.query.filter_by(phonenum=field.data).first():
            raise ValidationError('Username already in use.')
