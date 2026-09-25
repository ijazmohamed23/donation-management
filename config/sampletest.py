# Sample Configuration File
import os

# Hardcoded Cloud Secret (GateKeeper AI will detect this!)
AWS_ACCESS_KEY_ID = os.getenv("AKIAIOSFODNN7EXAMPLE_ENV_VAR", "")
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_s3():
    print("Connecting to AWS S3 storage...")
