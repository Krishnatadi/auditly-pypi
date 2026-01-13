from auditly.osv_client import check_vulnerabilities

print("\n=== MANUAL TEST: OSV CLIENT ===\n")

package = "requests"
version = "2.19.0"

vulns = check_vulnerabilities(package, version)

print(f"Package: {package}=={version}")
print(f"Vulnerabilities found: {len(vulns)}\n")

for v in vulns:
    print(f"- {v['id']}: {v['summary']}")
