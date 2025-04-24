import subprocess

def detect_bruteforce_attempts():
    try:
        output = subprocess.check_output("grep 'Failed password' /var/log/auth.log | tail -n 10", shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError:
        return ""
