from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(32)

# 티켓 발급 함수
def issue_ticket(id):
    if 'tickets' not in session:
        session['tickets'] = 5
        session['snacks'] = 0

    if session['tickets'] > 0:
        with open('id.txt', 'r') as file:
            valid_ids = [line.strip() for line in file]
        
        if id == valid_ids[0]:
            session['tickets'] -= 1
            session['snacks'] += 1
            return f"티켓을 발급받았습니다. 현재 발급 가능 티켓 수: {session['tickets']}, 현재 과자 수: {session['snacks']}"
        elif id == valid_ids[1]:
            session['tickets'] -= 1
            session['snacks'] += 2
            return f"티켓을 발급받았습니다. 현재 발급 가능 티켓 수: {session['tickets']}, 현재 과자 수: {session['snacks']}"
        else:
            return "유효하지 않은 id입니다."
    else:
        return f"티켓이 모두 소진되었습니다. 현재 발급 가능 티켓 수: {session['tickets']}, 현재 과자 수: {session['snacks']}"

# 티켓 초기화 함수
def reset_tickets():
    session['tickets'] = 5
    session['snacks'] = 0
    return f"티켓 발급 횟수가 초기화되었습니다. 현재 발급 가능 티켓 수: {session['tickets']}, 현재 과자 수: {session['snacks']}"

# 현재 티켓 수 반환 함수
def get_ticket_count():
    return session.get('tickets', 0)

# 현재 과자 수 반환 함수
def get_snacks_count():
    return session.get('snacks', 0)

# 홈페이지 라우트
@app.route('/')
def index():
    return render_template('index.html', ticket_count=get_ticket_count(), snack_count=get_snacks_count())

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
    if get_snacks_count() >= 10:
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
    app.run(host='0.0.0.0', port=80, debug=False)