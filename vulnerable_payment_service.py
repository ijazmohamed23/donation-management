"""Vulnerable Payment Gateway Service.

This service contains intentional security vulnerabilities to demonstrate
GateKeeper AI's automated GitHub Pull Request security gating and remediation.

Vulnerabilities Included:
1. [CRITICAL] GK-005 / Gitleaks: Hardcoded AWS Secret Key and Stripe API Key (CWE-798)
2. [CRITICAL] GK-001 / ML-SQLi: Dynamic SQL Injection via f-string (CWE-89)
3. [CRITICAL] GK-002: Remote Command Injection via os.system (CWE-78)
4. [HIGH]     GK-003: Remote Code Execution via eval() (CWE-94)
5. [HIGH]     GK-004: Insecure Deserialization via pickle.loads() (CWE-502)
6. [HIGH]     GK-007: Path Traversal via unvalidated open() (CWE-22)
7. [HIGH]     GK-008: Server-Side Request Forgery (SSRF) via requests.get() (CWE-918)
8. [MEDIUM]   GK-006: Broken Cryptographic Hash using MD5 (CWE-327)
"""

import hashlib
import os
import pickle
import sqlite3
import requests

# ------------------------------------------------------------------------------
# 1. HARDCODED CREDENTIALS (CWE-798 - CRITICAL / GK-005 & Secret Rule)
# ------------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_API_SECRET_KEY = "sec_live_token_99887766554433221100aabbccddee"
JWT_SECRET_KEY = "super_secret_jwt_production_signing_key_987654321"


def process_payment_transaction(user_id: str, card_token: str, order_id: str):
    """Processes a payment transaction with multiple critical vulnerabilities."""
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()

    # --------------------------------------------------------------------------
    # 2. SQL INJECTION (CWE-89 - CRITICAL / GK-001 & ML Detector)
    # Dynamic string interpolation allows an attacker to inject SQL payloads.
    # --------------------------------------------------------------------------
    query = f"SELECT balance, status FROM accounts WHERE user_id = '{user_id}' AND active = 1"
    cursor.execute(query)
    account = cursor.fetchone()

    # --------------------------------------------------------------------------
    # 3. COMMAND INJECTION (CWE-78 - CRITICAL / GK-002)
    # Direct shell execution with untrusted user input allows arbitrary command execution.
    # --------------------------------------------------------------------------
    os.system(f"curl -X POST https://audit.internal.net/log?order={order_id}")

    return account


def calculate_discount(order_amount: float, discount_formula: str):
    """Calculates discount using dynamic expression evaluation.
    
    --------------------------------------------------------------------------
    4. ARBITRARY CODE EXECUTION (CWE-94 - HIGH / GK-003)
    Unsafe eval() evaluates arbitrary Python expressions passed from users.
    --------------------------------------------------------------------------
    """
    discount = eval(discount_formula)
    return order_amount - discount


def restore_user_session(session_payload: bytes):
    """Restores user session state from raw binary data.
    
    --------------------------------------------------------------------------
    5. INSECURE DESERIALIZATION (CWE-502 - HIGH / GK-004)
    pickle.loads() can execute arbitrary OS commands embedded in payloads.
    --------------------------------------------------------------------------
    """
    session_data = pickle.loads(session_payload)
    return session_data


def download_receipt(customer_dir: str, filename: str):
    """Downloads an invoice receipt from disk.
    
    --------------------------------------------------------------------------
    6. PATH TRAVERSAL (CWE-22 - HIGH / GK-007)
    Direct string concatenation allows reading arbitrary files (e.g., ../../etc/passwd).
    --------------------------------------------------------------------------
    """
    file_path = customer_dir + "/" + filename
    with open(file_path, "r") as f:
        return f.read()


def notify_webhook_endpoint(target_callback_url: str):
    """Dispatches webhook notification to customer-supplied URL.
    
    --------------------------------------------------------------------------
    7. SERVER-SIDE REQUEST FORGERY (CWE-918 - HIGH / GK-008)
    Untrusted outbound HTTP request allows port scanning or AWS metadata extraction.
    --------------------------------------------------------------------------
    """
    response = requests.get(target_callback_url, timeout=5)
    return response.status_code


def generate_customer_hash(user_pin: str):
    """Hashes a user PIN.
    
    --------------------------------------------------------------------------
    8. WEAK CRYPTOGRAPHY (CWE-327 - MEDIUM / GK-006)
    MD5 is cryptographically broken and prone to collision attacks.
    --------------------------------------------------------------------------
    """
    pin_hash = hashlib.md5(user_pin.encode()).hexdigest()
    return pin_hash
