
from flask import Flask, request,redirect,url_for, jsonify, render_template,session
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'YJhCmVseWc'
app.config['MYSQL_PASSWORD'] = 'qowlYr4pay'
app.config['MYSQL_DB'] = 'YJhCmVseWc'

mysql = MySQL(app)

