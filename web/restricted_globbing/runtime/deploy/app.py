from flask import Flask, request, render_template, session, redirect, abort
from model.dml import findUser, join
from hashlib import sha256
from re import search
from os import urandom
import subprocess


app = Flask(__name__)
app.secret_key = urandom(32)

try:
    FLAG = open("/flag.txt", "r").read()
except:
    FLAG = "hihi"


@app.route("/", methods=["GET"])
def index():
    if not session:
        return render_template("login.html")
    
    elif session["role"] == "admin":
        return render_template("admin.html")
    
    elif session["role"] == "guest":
        return render_template("index.html", msg="Hello guest. Please upgrade your role!")

    else:
        return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("id")
        password = request.form.get("pw")

        if username == "" or password == "":
            return render_template("login.html", msg="Please give me the id and password")

        sha256_password = sha256((password).encode()).hexdigest()

        try:
            user = findUser(username, sha256_password)

            if user:
                if user[1].startswith("admin"):
                    session["username"] = user[1]
                    session["role"] = "admin"

                    return redirect("/admin")
                
                else:
                    session["username"] = user[1]
                    session["role"] = "guest"

                    return redirect("/")
                
            else:
                return render_template("login.html", msg="Login fail")
            
        except Exception as e:
            abort(500)


@app.route("/join", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("join.html")

    if request.method == "POST":
        username = request.form.get("id")
        password = request.form.get("pw")

        if username == "" or password == "":
            return render_template("join.html", msg="Enter username and password")

        # regex
        m = search(r".*", username) 

        if username or m:
            if m.group().strip().find("admin") == 0:
                return render_template("join.html", msg="admin is not allowed"), 403
            else:
                username = username.strip()
                sha256_password = sha256((password).encode()).hexdigest()
                join(username, sha256_password)
                return redirect("/login")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session:
        return redirect("/login")
    
    if session["role"] != "admin":
        return  """
            <script>alert('You are not admin')</script>
            <script>location.href='/'</script>
"""

    if request.method == "GET":
        return render_template("admin.html")

    # code please
    if request.method == "POST":
        url = request.form["url"].strip()

        if (url[0:4] != "http") or (url[7:34] != "jalnik.vercel.app/introduce"):
            return render_template("admin.html", msg="Not allowed URL")

        if (".." in url) or ("%" in url):
            return render_template("admin.html", msg="Not allowed path traversal")
        
        if url.endswith("secret"):
            return render_template("admin.html", msg="Not allowed string or character")
        try:
            response = subprocess.run(
                ["curl", f"{url}", "-m", "1"], capture_output=True, text=True, timeout=2
            )
            return render_template("admin.html", msg=response.stdout)

        except subprocess.TimeoutExpired:
            return render_template("admin.html", msg="Timeout !!!")


@app.route("/secret", methods=["GET"])
def flag():
    ip_address = request.remote_addr
    if ip_address == "127.0.0.1":
        return FLAG
    else:
        return "Only local access allowed", 403


app.run(host="0.0.0.0", port=80)
