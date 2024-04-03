from flask import Flask, render_template, render_template_string, request
import secrets
import string
import os

def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# killer secret? can you guess?
secret_code = generate_random_string(128)
print(secret_code)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')







@app.route('/membership')
def killer():
    code = request.args.get('secretcode',"enter the secret code")

    filter_list = ['cat', 'flag', 'chmod', 'rm', 'mv', 'nc', 'tcp', 'kill', 'halt', 'restart', 'shutdown', 'reboot']

    print(f"code: {code}")

    # show killer list
    if code == secret_code:

        memberList = ""

        try:
            with open('/etc/passwd', 'r') as f:
                memberList = f.readlines()
        except:
            memberList = "김진만 99년생"


        return memberList

    for filter in filter_list:
        if filter in code:
            return "I love Cat😺😺 no hack"

    render_template = """
    <!DOCTYPE html>
    <html>
    <head>

        <title>김진만 쇼핑몰</title>
    </head>
    <body>
    <div class="center-text">
        <div>
        <form method="GET">
            <label for="secret">Code please<br/></label>
            <input id="secret" name="secretcode" type="text" width="30px">
            <button type="submit">submit</button>
            </form>
            <p>%s {{no}}</p>
        </div>
    </div>
    </body>
    </html>

"""% code

    return render_template_string(render_template, no = "" if code == "enter the secret code" else "is not secret code")



if __name__=="__main__":
    app.run(host="0.0.0.0", debug=False, port= 80)