from flask import Flask, request, render_template, session, redirect, abort
from model.dml import findUser
from hashlib import sha256
import base64
import random


app = Flask(__name__)

# 누가 만든 쿠키~
members = ['Hanni1','Hanni2','Hanni3','Hanni4','Hanni5',
        'Minji1','Minji2','Minji3','Minji4','Minji5',
        'Haerin1','Haerin2','Haerin3','Haerin4','Haerin5', 
        'Daniel1','Daniel2','Daniel3','Daniel4','Daniel5',
        'Hyein1', 'Hyein2', 'Hyein3', 'Hyein4', 'Hyein5']

member = random.choice(members)


app.secret_key = member

try:
    FLAG = open("/flag.txt", "r").read()
except:
    FLAG = "문제가 생겼으니 관리자에게 문의하세요"


@app.route("/", methods=["GET"])
def index():
    if not session:
        return render_template("login.html")
    
    elif session["isAdmin"] == True:
        return render_template("index.html", role = "admin")
    
    elif session["isAdmin"] == False:
        return render_template("guest.html")

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
                if user[1] == ("admin"):
                    session["username"] = user[1]
                    session["isAdmin"] = True

                    return redirect("/admin")
                
                else:
                    session["username"] = user[1]
                    session["isAdmin"] = False

                    return redirect("/")
                
            else:
                return render_template("login.html", msg="Login fail")
            
        except Exception as e:
            abort(500)



@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session:
        return redirect("/login")
    
    if session["isAdmin"] == False:
        return  """
            <script>alert('You are not admin')</script>
            <script>location.href='/'</script>
"""

    if request.method == "GET":
        return render_template("admin.html")

    # code please
    if request.method == "POST":
        memberName = request.form["name"].strip()

        # .\./
        keyWordList = ["passwd", "py"]

        for keyword in keyWordList:
            
            # haha
            if keyword in memberName:
                return render_template('admin.html', msg="GET OUT")


        path = "/app/static/members/" + memberName

        # 뉴~ 진스
        try:
            with open(path, 'rb') as f:
                data = f.read()
            # HTML 템플릿에 인코딩된 이미지 데이터를 전달합니다.
            return render_template('admin.html', msg=data.decode('utf-8'))    
        except:
            return render_template('admin.html', msg="잘못된 형식입니다.")


        
app.run(host="0.0.0.0", port=80, debug=True)