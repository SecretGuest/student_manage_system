from flask import Blueprint, render_template,request,redirect,views
from student_manage_system.mystudent_sql import sqlconn
# WTForms
from wtforms.fields import simple
from wtforms import Form, validators

loginstu = Blueprint('loginstu',__name__)

class LoginForm(Form):
    # 用户名
    username = simple.StringField(
        label='用户名',  # label标签
        validators=[  # 校验规则
            validators.data_required(message='数据不能为空'),
            validators.Length(min=5,max=16,message="用户名要在5-6个字符之间")
        ],
        render_kw = {"class":'user'} # input标签中的类
    )
    # 密码
    pwd = simple.PasswordField(
        label='密码',  # label标签
        validators=[  # 校验规则
            validators.data_required(message='数据不能为空'),
            validators.Length(min=5, max=16, message="用户名要在5-6个字符之间"),
            validators.Regexp(regex='^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$',message='最少6位，包括至少1个大写字母，1个小写字母，1个数字，不允许包含特殊字符')
        ],
        render_kw={"class": 'pwd'}  # input标签中的类
    )
# CBV
class LoginView(views.MethodView):
    def get(self):
        loginfm = LoginForm()
        return render_template('login1.html', loginfm = loginfm)
    def post(self):
        msg = ''
        loginfm = LoginForm(request.form)
        if not loginfm.validate():
            return render_template('login1.html', loginfm=loginfm)
        sql = 'select * from user'
        ret = sqlconn(sql)
        # 获取name
        username = loginfm.data.get('username')
        pwd = loginfm.data.get('pwd')
        for stu in ret:
            user = stu[1]
            password = stu[2]
            if user == username and password == pwd:
                return redirect('/list_stu')
            else:
                msg = '用户名密码错误！'
        return render_template('login1.html', loginfm = loginfm, msg = msg)

loginstu.add_url_rule('/login',endpoint=None,view_func=LoginView.as_view(name='LoginView'))