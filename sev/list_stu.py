from flask import Blueprint, render_template
from student_manage_system.mystudent_sql import sqlconn

liststu = Blueprint('liststu',
                    __name__,
                    template_folder='bluetemplates',
                    static_folder='static'
                    )


@liststu.route('/list_stu')
def list():
    sql = 'select * from students_info'
    ret = sqlconn(sql)
    return render_template('stu_list.html', ret=ret)