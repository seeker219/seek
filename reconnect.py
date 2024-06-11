import random
import subprocess

random_port = random.randint(30000, 59000)
command = [
    "/usr/bin/ssh",
    "-N",
    "-v",
    "-C",
    "-p", "443",
    "-i", "/root/.ssh/remote.pem",
    "-o", "StrictHostKeyChecking=no",
    "-o", "ServerAliveInterval=30",
    "-o", "ServerAliveCountMax=2880",
    "ubuntu@vnc.envtec.de",
    f"-R {random_port}:127.0.0.1:22"
]

subprocess.run(command)
