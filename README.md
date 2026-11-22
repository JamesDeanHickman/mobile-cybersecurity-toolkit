
# Mobile Cybersecurity Toolkit

A hands-on cybersecurity learning project developed using Python and GitHub Codespaces.

## Project 01: File Integrity Monitor

A Python-based defensive security utility that uses SHA-256 cryptographic hashing to detect file modifications.

### Features
- SHA-256 file hashing
- Trusted file baseline creation
- File integrity verification
- Modification detection
- Missing-file detection
- JSON baseline storage

### Testing and Results

| Test | Expected Result | Outcome |
|---|---|---|
| Generate SHA-256 hash | 64-character digest | PASS |
| Check unchanged file | UNCHANGED | PASS |
| Modify monitored file | MODIFIED | PASS |

### Technologies
- Python 3
- SHA-256
- JSON
- GitHub Codespaces
- Linux environment

### Learning Objectives
- Understand cryptographic hashing
- Explore the avalanche effect
- Practice defensive security monitoring
- Learn baseline-based integrity verification

### Security Considerations

This is an educational prototype. Its baseline is stored locally and is not protected against an attacker who can modify both the monitored files and baseline.

Future improvements will include baseline protection, stronger error handling, and automated reporting.

### Automated Unit Tests

The project includes a Python unittest suite covering:

- Consistency of SHA-256 hash generation
- Detection of file content changes
- Correct SHA-256 digest length
- Handling of missing files

Test command:

python -m unittest discover -s tests -v

Latest test results: 4 tests passed.S