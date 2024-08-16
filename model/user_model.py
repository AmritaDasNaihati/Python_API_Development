import mysql.connector
import json
from flask import make_response


class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="root",database="user_details")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("connection Successfull")
        except:
            print("some error, Please check")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM user_table")
        result = self.cur.fetchall()
        if len(result)>0:
            # return json.dump(result)
            #return make_response({"payload":result}, 200)
            res = make_response({"payload":result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            return make_response({"message": "No data available in that table"}, 204)

    def user_adduser_model(self, data):
        self.cur.execute(f"INSERT into user_table(UserName, Email, Role, Password, PhoneNo) VALUES('{data['UserName']}', '{data['Email']}', '{data['Role']}', '{data['Password']}', '{data['PhoneNo']}')")
        return make_response({"message": "user added successfully"}, 201)

    def user_updateuser_model(self, data):
        self.cur.execute(f"UPDATE user_table SET UserName='{data['UserName']}', Email='{data['Email']}', Role='{data['Role']}', Password='{data['Password']}', PhoneNo='{data['PhoneNo']}' WHERE UserID={data['UserID']}")
        if self.cur.rowcount > 0:
            return make_response({"message": "user updated successfully"}, 201)
        else:
            return make_response({"message": "Nothing to update"}, 202)

    def user_deleteuser_model(self, id):
        self.cur.execute(f"DELETE FROM user_table WHERE UserID={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "user deleted successfully"}, 200)
        else:
            return make_response({"message": "Nothing to delete"}, 202)

    def user_updateUserSingleElement_model(self, data, id):
        qry = "UPDATE user_table SET "
        for key in data:
            qry = qry + f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE UserID={id}"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": "user updated successfully"}, 201)
        else:
            return make_response({"message": "Nothing to update"}, 202)

    def user_getSingleUser_model(self, id):
        self.cur.execute(f"SELECT * FROM user_table WHERE UserID={id}")
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"payload": result}, 200)
        else:
            return make_response({"message": "No data available in that table"}, 204)
