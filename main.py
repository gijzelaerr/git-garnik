from git import Repo, InvalidGitRepositoryError
from pathlib import Path
from sys import exit

here = Path(__file__).parent.absolute()

print(f"trying to extrach git branch for location '{here}'")

try:
    repo = Repo(here)
except InvalidGitRepositoryError:
    print(f"error: '{here}' is not a git repository")
    exit(2)
else:
    print(f"the current branch for '{here}' is '{repo.active_branch.name}")

