from passlib.context import CryptContext

# Set up password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
def get_password_hash(password):
    return pwd_context.hash(password)

# Verify the hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
