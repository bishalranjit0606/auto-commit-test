import os
import random
import subprocess
from datetime import datetime

# --- Configuration for Contribution Graph Fix ---
# Using your no-reply email ensures the commits count toward your contributions 
# without exposing your primary email.
GIT_USER_NAME = "bishalranjit0606"
GIT_USER_EMAIL = "bishalranjit0606@users.noreply.github.com"
# -----------------------------------------------

# Work in the current repository
repo_path = os.getcwd()
os.chdir(repo_path)

# ✅ Set Git author identity for all commits
subprocess.run(["git", "config", "user.name", GIT_USER_NAME], check=True)
subprocess.run(["git", "config", "user.email", GIT_USER_EMAIL], check=True)

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

# Note: The 'git push' command is removed from here and handled by the workflow.
print("✅ All commits done for this run — changes are ready to push.")
