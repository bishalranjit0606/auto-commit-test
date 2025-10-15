import os
import random
import subprocess
import time
from datetime import datetime

# Path to your repo
repo_path = "/Users/bishalranjitkar/desktop/Bishal_ranjit/auto-commit-test"
os.chdir(repo_path)

# Choose random number of commits between 20–30
num_commits = random.randint(20, 30)
print(f"Making {num_commits} commits today...")

for i in range(num_commits):
    filename = "auto_file.txt"

    # Append a new line each time
    with open(filename, "a") as f:
        f.write(f"Commit {i+1} at {datetime.now()}\n")

    # Git add + commit
    subprocess.run(["git", "add", filename])
    commit_message = f"Auto commit {i+1} at {datetime.now()}"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Small pause (1–5 seconds)
    wait = random.randint(1, 5)
    print(f"Commit {i+1} done, waiting {wait}s...")
    time.sleep(wait)

# Push all commits together
subprocess.run(["git", "push", "origin", "main"])
print("✅ All commits pushed!")

