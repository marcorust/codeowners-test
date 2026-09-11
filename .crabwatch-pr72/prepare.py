import os
from pathlib import Path
import shutil

case = os.environ["CASE"]
root = Path(".github")
shutil.rmtree(root)
clean = """name: Clean fixture
on: push
permissions: {}
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo hello
"""
finding = clean.replace("    steps:", "    env:\n      ACTIONS_ALLOW_UNSECURE_COMMANDS: 'true'\n    steps:")

def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

# This workflow is audit data only; it is never executed by GitHub Actions.
write("vendor/project/.github/workflows/finding.yml", finding)
if case == "root-clean-nested-finding":
    write(".github/workflows/clean.yml", clean)
elif case == "root-finding":
    write(".github/workflows/finding.yml", finding)
elif case == "empty-root":
    root.mkdir()
elif case == "empty-workflows":
    (root / "workflows").mkdir(parents=True)
elif case == "root-docs-only":
    write(".github/README.md", "No workflows here.\n")
elif case == "root-hidden-file-only":
    write(".github/.keep", "placeholder\n")
elif case != "missing-root":
    raise ValueError(case)
print(f"Prepared {case}; nested finding fixture is always present")
