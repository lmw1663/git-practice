import os
import subprocess
import requests

# 하드코딩된 비밀번호 
DB_PASSWORD = "super_secret_password"  # hardcoded password

def bad_eval(user_input: str):
    # 사용자 입력을 그대로 eval (code injection 위험)
    return eval(user_input)  # semgrep: python.lang.security.audit.eval

def bad_subprocess(cmd: str):
    # shell=True 로 사용자 입력 실행 (command injection 위험)
    subprocess.run(cmd, shell=True)  # semgrep: subprocess shell=True

def bad_requests():
    # SSL 검증 끄기 (MITM 공격 위험)
    requests.get("https://example.com", verify=False)  # semgrep: requests.verify_false

if __name__ == "__main__":
    bad_subprocess("ls")
    bad_eval("1+1")
    bad_requests()
    print("done")