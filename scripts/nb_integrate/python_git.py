import pygit2
import os

import fnmatch
import glob
from pathlib import Path

here = os.path.dirname(__file__)

class nb_repo(object):
    """ Class containing methods used to
    identify the notebooks committed to the
    repository and add the SHA to the Jinja template"""

    def __init__(self, here):
        try:
            repo_path = pygit2.discover_repository(here)
            repo = pygit2.Repository(repo_path)
            self.repository = repo
        except:
            raise IOError ('This does not seem to be a repository')

# The reference log
for commit in repo.head.log():
    print(commit.oid_new.hex, commit.message)

def check_log():
    """ Check the number of commits be"""
    all_commits = [commit for commit in repo.head.log()]
    if len(all_commits) <= 1:
        print('Only one commit: converting all notebooks')
        notebooks  = find_notebooks()
    else:
        print('Finding the last commit only')
    return notebooks


def find_notebooks():
    """ Find all the notebooks in the repo, but excludes those
    in the _site folder, this will be default if no specific
    notebook was passed for conversion
    """

    basePath = Path(os.getcwd())
    notebooksAll = [nb for nb in glob.glob('**/*.ipynb')]
    exception = os.path.join(basePath , '/_site/*/*')
    notebooks = [nb for nb in notebooksAll if not fnmatch.fnmatch(nb, exception)]
    return notebooks