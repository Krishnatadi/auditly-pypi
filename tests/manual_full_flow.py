import subprocess
import sys

print("\n=== MANUAL TEST: FULL FLOW ===\n")

cmd = [sys.executable, "-m", "auditly"]

print("Running:", " ".join(cmd))
subprocess.run(cmd)
