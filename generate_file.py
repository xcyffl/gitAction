#!/usr/bin/env python3

import datetime
import os
from pathlib import Path

output_dir = Path("generated")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "build_info.txt"
output_file.write_text(
    f"Generated at: {datetime.datetime.utcnow().isoformat()}Z\n"
    f"Commit SHA: {os.environ.get('GITHUB_SHA', 'unknown')}\n"
)

print(f"Wrote {output_file}")

