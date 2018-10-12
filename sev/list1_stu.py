from flask import Blueprint, render_template
from student_manage_system.mystudent_sql import sqlconn

list1stu = Blueprint('list1stu',
                    __name__,
                    template_folder='bluetemplates',
                    )


@list1stu.route('/list1_stu/<int:id>')
def list(id):
    id = int(id)
    sql = "select * from students_info where id = %s" %id
    ret = sqlconn(sql)
    return render_template('stu_list1.html', ret=ret)