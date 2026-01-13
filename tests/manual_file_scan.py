from auditly.file_scanner import scan_requirements
import tempfile

print("\n=== MANUAL TEST: FILE SCAN ===\n")

with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
    f.write("""
requests==2.19.0
flask==0.12
""")
    path = f.name

results = scan_requirements(path)

print("\nScan completed.")
print(f"Vulnerable packages found: {len(results)}")

for r in results:
    print(r)
