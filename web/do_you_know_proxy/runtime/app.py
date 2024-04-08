from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from threading import Thread, Lock
import os


app = Flask(__name__)
CORS(app)

tickets = 5
snacks = 0
lock = Lock()
app.secret_key = os.urandom(32)


# 티켓 발급 함수x``
def issue_ticket(id):
    global tickets, snacks
    with open('id.txt', 'r') as file:
        valid_ids = [line.strip() for line in file]
    with lock:
        if tickets > 0:
            if id == valid_ids[0]:
                tickets -= 1
                snacks += 1
                return f"티켓을 발급받았습니다. 현재 발급 가능 티켓 수: {tickets}, 현재 과자 수: {snacks}"
            elif id == valid_ids[1]:
                tickets -= 1
                snacks += 2
                return f"티켓을 발급받았습니다. 현재 발급 가능 티켓 수: {tickets}, 현재 과자 수: {snacks}"
            else:
                return "유효하지 않은 id입니다."
        else:
            return f"티켓이 모두 소진되었습니다. 현재 발급 가능 티켓 수: {tickets}, 현재 과자 수: {snacks}"

# 티켓 초기화 함수
def reset_tickets():
    global tickets, snacks
    with lock:
        tickets = 5
        snacks = 0
        return f"티켓 발급 횟수가 초기화되었습니다. 현재 발급 가능 티켓 수: {tickets}, 현재 과자 수: {snacks}"

# 현재 티켓 수 반환 함수
def get_ticket_count():
    global tickets
    with lock:
        return tickets

# 현재 과자 수 반환 함수
def get_snacks_count():
    global snacks
    with lock:
        return snacks

# 홈페이지 라우트
@app.route('/')
def index():
    return render_template('index.html', ticket_count=get_ticket_count())

# 티켓 발급 라우트
@app.route('/get_ticket', methods=['POST'])
def get_ticket():
    try:
        data = request.get_json()
        id = data.get('id')
        result = issue_ticket(id)
        return jsonify({"message": result, "ticket_count": get_ticket_count(), "snack_count": get_snacks_count()})
    except Exception as e:
        return jsonify({"message": str(e), "ticket_count": get_ticket_count(), "snack_count": get_snacks_count()}), 500

# 티켓 초기화 라우트
@app.route('/reset_ticket', methods=['POST'])
def reset_ticket_route():
    try:
        result = reset_tickets()
        return jsonify({"message": result, "ticket_count": get_ticket_count(), "snack_count": get_snacks_count()})
    except Exception as e:
        return jsonify({"message": str(e), "ticket_count": get_ticket_count(), "snack_count": get_snacks_count()}), 500

# 과자 교환 라우트
@app.route('/trade_snack', methods=['POST'])
def trade_snack():
    global snacks
    
    if snacks >= 10:
        # 과자 개수가 10개 이상인 경우, flag.txt 파일의 내용을 클라이언트에게 전송합니다.
        flag_content = read_flag()
        return jsonify({"message": "You have enough snacks!", "flag": flag_content})
    else:
        # 과자 개수가 10개 미만인 경우, 적절한 응답을 전송합니다.
        return jsonify({"message": "You need more snacks to get the flag."})

def read_flag():
    # flag.txt 파일을 읽어와서 내용을 반환합니다.
    with open('flag.txt', 'r') as file:
        flag_content = file.read()
    return flag_content

if __name__ == '__main__':
    app.run(debug=True)
