from auditly.risk import calculate_risk_score

print("\n=== MANUAL TEST: RISK SCORE ===\n")

mock_vulns = [
    {
        "severity": [
            {"type": "CVSS_V3", "score": "9.8"},
            {"type": "CVSS_V3", "score": "5.0"}
        ]
    }
]

score = calculate_risk_score(mock_vulns)

print("Expected score: 14.8")
print(f"Calculated score: {score}")
