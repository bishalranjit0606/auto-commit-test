import os
import random
import subprocess
from datetime import datetime

# Work in the current repository
repo_path = os.getcwd()
os.chdir(repo_path)

# ✅ Set Git author identity for all commits
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "actions@github.com"], check=True)

# Decide 1–5 commits per run
num_commits = random.randint(1, 5)
print(f"🌞 Planning {num_commits} commits for this run")

for i in range(1, num_commits + 1):
    # Write a new line to file
    filename = "auto_file.txt"
    with open(filename, "a") as f:
        f.write(f"Commit {i} at {datetime.now()}\n")

    # Git add + commit
    subprocess.run(["git", "add", filename], check=True)
    msg = f"Auto commit {i} at {datetime.now()}"
    subprocess.run(["git", "commit", "-m", msg])

print("✅ All commits done for this run — pushing to GitHub…")
subprocess.run(["git", "push", "origin", "main"])
print("✅ Push complete!")

