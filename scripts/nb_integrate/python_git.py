import pygit2
import os

# look for a git repository

here = os.path.dirname(__file__)
repo_path = pygit2.discover_repository(here)
repo = pygit2.Repository(repo_path)

# The reference log
head = repo.references.get('refs/heads/master')
for commit in head.log():
    print(commit.oid_new.hex, commit.message)

# Find the last commit
last_commit = repo[repo.head.target]
commit_sha1 = last_commit.oid.hex[0:7]

git show - -name - status - -oneline

def check_commits():
    if len(head.log) == 1:
        notebooks = find_notebooks()
    else:
        notebooks = nb_git()
    for nb in notebooks():
        convert_single_nb(nb)


