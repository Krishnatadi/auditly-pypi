![PyPI Version](https://img.shields.io/pypi/v/auditly.svg)
![Dependencies](https://img.shields.io/librariesio/release/pypi/auditly)
![PyPI - License](https://img.shields.io/pypi/l/auditly)


# Auditly

**Auditly** is an enterprise-ready dependency vulnerability auditing tool designed for modern developers and organizations.  
It goes beyond traditional scanners by detecting vulnerabilities not only in **direct dependencies**, but also in **sub-dependencies (transitive dependencies)** — a critical security gap in many tools today.

Auditly focuses on **actionable security**, helping developers quickly understand risks, fix issues, and maintain secure dependency chains.

---

## Why Auditly?

Most dependency scanners stop at direct dependencies.  
Auditly goes deeper.

-Detects vulnerabilities hidden inside sub-dependencies  
-Provides clear fix suggestions  
-Clean, developer-friendly CLI output  
-Ready for CI/CD and enterprise pipelines  

---

## Features

| Feature | Description | Availability |
|---------|-------------|-------------|
| **Direct dependency scan** | Scans all installed packages or packages in a `requirements.txt` file | Yes | 
| **Fix suggestions** | Shows exact `pip install <package>==<version>` commands to fix vulnerabilities | Yes |
| **Summary stats** | Displays total packages scanned and total vulnerabilities | Yes |
| **Optional transitive scan** | Scans all sub-dependencies recursively (use `--transitive`) | Yes |
| **JSON output** | Pretty JSON output for CI/CD pipelines (use `--json`) | Yes |
| **Requirements.txt scan** | Scan packages listed in a requirements file | Yes |
---

## Installation

This package is available through the [PyPI registry](__https://pypi.org/project/random-password-toolkit/__).

Before installing, ensure you have Python 3.6 or higher installed. You can download and install Python from [python.org](__https://www.python.org/downloads/__).

You can install the package using `pip`:

```bash
pip install auditly

```
---

### What Makes Auditly Unique?

| Capability                    | Traditional Tools | Auditly |
|-------------------------------|-------------------|---------|
| Direct dependency scan        | Supported         | Supported |
| Sub-dependency scan           | Not supported     | Supported |
| Fix recommendations           | Not supported     | Supported |
| Progress feedback             | Not supported     | Supported |
| Clean summary statistics      | Not supported     | Supported |


---

## Usage

Auditly can be run as a CLI tool. Below is a summary of all available commands and flags.

| Command / Flag        | Description                                                         | Example                          |
|-----------------------|---------------------------------------------------------------------|----------------------------------|
| `-r`, `--requirements` | Scan a `requirements.txt` file instead of the installed environment | `auditly -r requirements.txt`    |
| `--json`              | Output results in JSON format with detailed issue resolution info, useful for CI/CD                     | `auditly --json`                 |
| `--transitive`        | Scan all sub-dependencies recursively (deep scan)                  | `auditly --transitive`           |


---

## Examples
### 1. Default scan of installed environment

```bash
auditly
```

**Output:**

```text
[auditly] Vulnerability Scan Summary
Total Packages Scanned      : 10
Total Vulnerabilities Found : 2

Package     : flask==0.12
Risk Score  : 10
  - CVE-2018-1000656: Flask <0.12.3 XSS
    → Suggested fix: pip install flask==0.12.3
------------------------------------------------------------
Package     : somepkg==1.0
Risk Score  : 7
  - CVE-XXXX-YYYY: Some vulnerability
    → No fix available. Try contacting package developers
------------------------------------------------------------
```

### 2. Scan `requirements.txt`

```bash
auditly -r requirements.txt
```
---

### 3. Deep / Transitive Scan (Sub-dependencies)

```bash
auditly --transitive
```

Scans all installed packages including their sub-dependencies.

Alerts for deprecated / EOL packages.

Progress bar shows scan progress.

---

### 4. JSON Output (CI/CD pipelines)

```bash
auditly --json
```

**Output:**

```json
{
    "summary": {
        "total_packages_scanned": 10,
        "total_vulnerabilities_found": 2
    },
    "results": [
        {
            "package": "flask",
            "version": "0.12",
            "risk_score": 10,
            "vulnerabilities": [
                {
                    "id": "CVE-2018-1000656",
                    "summary": "Flask <0.12.3 XSS",
                    "fix_version": "0.12.3",
                    "references": [
                        "https://nvd.nist.gov/vuln/detail/CVE-2018-1000656"
                        ]
                }
            ]
        }
    ]
}
```

---
## Discussions
- **GitHub Discussions**: Share use cases, report bugs, and suggest features.

We'd love to hear from you and see how you're using **Auditly** in your projects!

---

## Requesting Features
If you have an idea for a new feature, please open a feature request in the Issues section with:
- A clear description of the feature
- Why it would be useful

---

## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/auditly-python/issues). We actively monitor and respond to community feedback.

---


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishnatadi/auditly-python/blob/main/LICENSE) file for details.