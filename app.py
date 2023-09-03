from flask import Flask

# Flask 애플리케이션을 생성합니다.
app = Flask(__name__)

# 루트 URL에 대한 라우팅 및 처리 함수를 정의합니다.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 애플리케이션 실행
if __name__ == '__main__':
    app.run()