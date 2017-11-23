import pygit2
import os


# look for a git repository

wdir =  os.getcwd()
repo_path = pygit2.discover_repository(wdir)
repo = pygit2.Repository(repo_path)


# The reference log
head = repo.references.get('refs/heads/master')
for entry in head.log():
    print(entry.message)