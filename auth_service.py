"""Sample Vulnerable Service for GateKeeper AI Testing.

This file contains intentional security flaws designed to test:
- Rule GK005: Hardcoded API Secret Keys
- Rule GK001: SQL Injection via Dynamic String Concatenation
- Rule GK002: Command Injection via os.system
- Rule GK004: Insecure Deserialization via pickle.loads
- Rule GK006: Broken Cryptographic Hash (MD5)
"""

import hashlib
import os
import pickle
import sqlite3

# 1. Hardcoded Secret (CWE-798 / Rule GK005)
STRIPE_API_SECRET_KEY = "sk_live_99887766554433221100aabbccddeeff"


def get_user_profile(user_id: str, raw_payload: bytes):
    # 2. SQL Injection Vulnerability (CWE-89 / Rule GK001)
    query = "SELECT * FROM users WHERE id = " + user_id
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)

    # 3. Command Injection Vulnerability (CWE-78 / Rule GK002)
    os.system("ping -c 1 " + user_id)

    # 4. Insecure Deserialization (CWE-502 / Rule GK004)
    user_state = pickle.loads(raw_payload)

    # 5. Broken Cryptography (CWE-327 / Rule GK006)
    auth_token_hash = hashlib.md5(user_id.encode()).hexdigest()

    return cursor.fetchall(), user_state, auth_token_hash
