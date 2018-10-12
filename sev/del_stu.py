from flask import Blueprint, request,redirect
from student_manage_system.mystudent_sql import sqlconn


delstu = Blueprint('delstu',__name__)


@delstu.route('/del_stu')
def delate():

    id = int(request.args["id"])
    print(id)
    sql = "delete from students_info where id = %s" %id
    sqlconn(sql,change=True)
    # cursor.close()
    # connect.close()

    return redirect('/list_stu')