from auditly.env_scanner import scan_environment

print("\n=== MANUAL TEST: ENVIRONMENT SCAN ===\n")

results = scan_environment()

print("\nScan completed.")
print(f"Total vulnerable packages found: {len(results)}")

for r in results[:5]:  # show first 5 only
    print(r)
