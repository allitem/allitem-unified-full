import subprocess, json
def run(repo, payload):
    cmd = f"{repo['entry']} '{json.dumps(payload)}'"
    return subprocess.check_output(cmd, shell=True).decode()
