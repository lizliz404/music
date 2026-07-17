import subprocess, os

prompt = open('/home/ubuntu/music/07-17-grow-the-fuck-up/raw-prompt-gpt-5.6-sol.txt').read()

result = subprocess.run(
    ['/home/ubuntu/.local/bin/agent', '-p', '-f',
     '--model', 'cursor-grok-4.5-high',
     '--workspace', '/home/ubuntu/music/07-17-grow-the-fuck-up',
     '--yolo', '--output-format', 'text', prompt],
    capture_output=True, text=True, timeout=900,
    cwd='/home/ubuntu/music/07-17-grow-the-fuck-up'
)

open('/home/ubuntu/music/07-17-grow-the-fuck-up/grok45-high-raw-stdout.txt', 'w').write(result.stdout or '')
open('/home/ubuntu/music/07-17-grow-the-fuck-up/grok45-high-raw-stderr.txt', 'w').write(result.stderr or '')
print(f"exit_code={result.returncode}")
print(f"stdout_chars={len(result.stdout)}")
print(f"stderr_chars={len(result.stderr)}")
