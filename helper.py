import os
import subprocess
import requests
import sqlite3
import pickle
import tempfile

DB_PASSWORD = "super_secret_password"  # hardcoded password

def bad_eval(user_input: str):
    # 사용자 입력을 그대로 eval (code injection 위험)
    return eval(user_input)  # semgrep: python.lang.security.audit.eval

def bad_subprocess(cmd: str):
    # shell=True 로 사용자 입력 실행 (command injection 위험
    subprocess.run(cmd, shell=True)  # semgrep: subprocess shell=True

def bad_requests():
    # SSL 검증 끄기 (MITM 공격 위험
    requests.get("https://example.com", verify=False)  # semgrep: requests.verify_false



# ========== ERROR 레벨 ==========

# 1. 하드코딩된 비밀번호
SECRET_KEY = "my_secret_key_12345"  # ERROR
DB_PASSWORD = "admin123"  # ERROR

# 2. Command Injection
def run_command(user_input: str):
    subprocess.run(user_input, shell=True)  # ERROR

# 3. SSL 검증 비활성화
def insecure_api_call():
    requests.get("https://api.example.com", verify=False)  # ERROR
    requests.post("https://api.example.com", verify=False)  # ERROR

# 4. SQL Injection
def get_user(username: str):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"  # ERROR
    return conn.execute(query)

# ========== WARNING 레벨 =========

# 1. eval() 사용
def calculate(expression: str):
    return eval(expression)  # WARNING

# 2. pickle 사용
def load_data(data: bytes):
    return pickle.loads(data)  # WARNING

# 3. 임시 파일
def create_temp():
    return tempfile.mktemp()  # WARNING

# 4. exec() 사용
def execute_code(code: str):
    exec(code)  # WARNING



if __name__ == "__main__":
    bad_subprocess("ls")
    bad_eval("1+1")
    bad_requests()
    run_command("ls -la")
    calculate("1 + 1")
    insecure_api_call()
    print("done")