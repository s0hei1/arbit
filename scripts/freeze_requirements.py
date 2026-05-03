import subprocess
from pathlib import Path
import sys


def main():
    project_root = Path(__file__).parent.parent
    requirements_file = project_root / "requirements.txt"

    with requirements_file.open("w") as f:
        subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            cwd=project_root,
            stdout=f,
            check=True,
        )


if __name__ == "__main__":
    main()