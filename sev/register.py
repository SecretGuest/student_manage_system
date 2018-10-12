from flask import Blueprint, render_template,request,redirect,views,session
from student_manage_system.mystudent_sql import sqlconn
# WTForms
from wtforms.fields import simple,core
from wtforms import Form, validators


resstu = Blueprint('resstu',__name__)

# WTForms register

class RegForm(Form):
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
    # 确认密码
    repwd = simple.PasswordField(
        label='密码',  # label标签
        validators=[  # 校验规则
            validators.data_required(message='数据不能为空'),
            validators.EqualTo('pwd',message='两次密码不一致')
        ],
        render_kw={"class": 'repwd'}  # input标签中的类
    )
    # 单选
    gender = core.RadioField(
        label='性别',
        choices=(
            (1,'女'),
            (2,'男')
        ),
        coerce=int,  # 选择字符串转化为int 默认为str
        default=2 # 默认选中
    )

    # 多选
    hobby = core.SelectMultipleField(
        label='爱好',
        choices=[
            [1,'西游记'],
            [2, '红楼梦'],
        ],
        coerce=int,
        default=[1,2]   # 默认
    )

# CBV
class RegisterView(views.MethodView):
    def get(self):
        refm = RegForm()
        return render_template('register.html', refm = refm)
    def post(self):
        # 获取数据执行校验
        refm = RegForm(request.form)
        if not refm.validate():
            return render_template('register.html', refm = refm)

        # 获取username, pwd
        username = refm.data.get('username')
        pwd = refm.data.get('pwd')
        # flasksession
        session['user'] = username
        # 存储
        sql = "insert user(name,pwd) values('%s','%s')" % (username, pwd)
        sqlconn(sql,change=True)
        print('session',session.get('user'))
        return redirect('/list_stu')

resstu.add_url_rule('/register',endpoint=None,view_func=RegisterView.as_view(name='RegisterView'))