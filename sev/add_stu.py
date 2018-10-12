from flask import Blueprint, render_template,request,redirect
from student_manage_system.mystudent_sql import sqlconn


addstu = Blueprint('addstu',__name__)


@addstu.route('/add_stu',methods=('GET','POST'))
def add():
    met = request.method
    if met == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        print(type(name),type(age))
        sql = "insert students_info(name,age) values('%s',%d)" %(name,age)
        sqlconn(sql,change=True)
        # cursor.close()
        # connect.close()
        return redirect('/list_stu')
    return render_template('stu_add.html')