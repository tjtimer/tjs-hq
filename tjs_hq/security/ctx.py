"""
ctx.py
author: Tim "tjtimer" Jedro
created: 07.04.19
"""
from passlib.context import CryptContext

pwd_ctx = CryptContext(
    schemes=["pbkdf2_sha512"],
    pbkdf2_sha512__min_rounds=13666,
    pbkdf2_sha512__default_rounds=23666,
    pbkdf2_sha512__max_rounds=66666,
    deprecated='auto'
)
