from flask import Flask, request, redirect
import os
import subprocess
import sys
import sqlite3

app = Flask(__name__)

# check if the email (GET variable) is in the database users and if so, unsubscribe by deleting it
@app.route('/unsubscribe')
def unsubscribe():
    # get the email (GET variable)
    email = request.args.get('email')
    # get the database connection
    db = sqlite3.connect("users.db")
    # get the user's id
    user_id = db.execute(f"SELECT id FROM users WHERE email = {email}").fetchone()
    # delete the user's entry from the database
    db.execute(f"DELETE FROM users WHERE id = {user_id[0]}")
    # close the database connection
    db.close()
    # redirect to the unsubscribe page
    return redirect("/unsubscribe/")