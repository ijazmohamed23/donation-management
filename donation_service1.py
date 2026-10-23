"""Sample Payment & Donation Service for GateKeeper Security Gate Testing.

This service contains intentional security flaws designed to test:
- Rule GK005: Hardcoded Internal Credentials / API Token
- Rule GK001: SQL Injection via String Concatenation
- Rule GK002: Command Injection via os.system
- Rule GK003: Dangerous Dynamic Code Evaluation (eval)
- Rule GK004: Insecure Deserialization via pickle.loads
- Rule GK006: Broken Cryptographic Hash (MD5)
- Rule GK007: Path Traversal in File Access
"""

import hashlib
import os
import pickle
import sqlite3

# 1. Hardcoded Secret (CWE-798 / Rule GK005)
PAYMENT_GATEWAY_API_TOKEN = os.getenv("PAYMENT_GATEWAY_API_TOKEN", "")


def process_donor_donation(donor_id: str, donation_amount: str, receipt_payload: bytes):
    conn = sqlite3.connect("donations.db")
    cursor = conn.cursor()

    # 2. SQL Injection Vulnerability (CWE-89 / Rule GK001)
    sql_query = "SELECT * FROM donors WHERE id = " + donor_id
    cursor.execute(sql_query)

    # 3. Command Injection Vulnerability (CWE-78 / Rule GK002)
    os.system("ping -c 1 " + donor_id)

    # 4. Insecure Dynamic Code Evaluation (CWE-94 / Rule GK003)
    calculated_tax = eval(donation_amount + " * 0.05")

    # 5. Insecure Deserialization (CWE-502 / Rule GK004)
    donor_metadata = pickle.loads(receipt_payload)

    # 6. Broken Cryptography (CWE-327 / Rule GK006)
    donor_hash = hashlib.md5(donor_id.encode()).hexdigest()

    # 7. Path Traversal Vulnerability (CWE-22 / Rule GK007)
    with open("receipts/" + donor_id + ".txt", "w") as f:
        f.write(f"Donation: {donation_amount}")

    return cursor.fetchall(), donor_metadata, donor_hash, calculated_tax
