from flask import Flask
from student_manage_system.sev import update_stu
from student_manage_system.sev import list1_stu
from student_manage_system.sev import register
from student_manage_system.sev import login, add_stu, del_stu, list_stu
from redis import Redis
from flask_session import Session

app = Flask(__name__,template_folder='templates')
# session配置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1',port=6379,db=5)
Session(app)

app.register_blueprint(list_stu.liststu)  # 查看数据
app.register_blueprint(list1_stu.list1stu)  # 查看一条数据
app.register_blueprint(add_stu.addstu)  # 添加数据
app.register_blueprint(del_stu.delstu)  # 删除数据
app.register_blueprint(update_stu.updatestu)  # 跟新数据


app.register_blueprint(register.resstu) # 注册
app.register_blueprint(login.loginstu) # 登录

if __name__ == '__main__':
    app.run(debug=True)