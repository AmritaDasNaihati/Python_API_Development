from app import app
from model.user_model import user_model
from flask import request
from datetime import datetime


obj = user_model()


@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/user/adduser", methods=["POST"])
def user_adduser_controller():
    return obj.user_adduser_model(request.form)


@app.route("/user/updateuser", methods=["PUT"])
def user_updateuser_controller():
    return obj.user_updateuser_model(request.form)


@app.route("/user/deleteuser/<id>", methods=["DELETE"])
def user_deleteuser_controller(id):
    return obj.user_deleteuser_model(id)


@app.route("/user/updateUserSingleElement/<id>", methods=["PATCH"])
def user_updateUserSingleElement_controller(id):
    return obj.user_updateUserSingleElement_model(request.form, id)


@app.route("/user/getall/<id>", methods=["GET"])
def user_getSingleUser_controller(id):
    return obj.user_getSingleUser_model(id)


@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)


