from flask import Blueprint, render_template,request,redirect
from student_manage_system.mystudent_sql import sqlconn


updatestu = Blueprint('updatestu',__name__)


@updatestu.route('/update_stu',methods=('GET','POST'))
def update():
    met = request.method
    id = int(request.args['id'])
    if met == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        sql = "update students_info set name = '%s',age = %d where id = %d" % (name,age,id)
        sqlconn(sql,change=True)
        return redirect('/list_stu')
    sql = "select * from students_info where id=%s" %id
    ret = sqlconn(sql)

    return render_template('stu_update.html', ret = ret)