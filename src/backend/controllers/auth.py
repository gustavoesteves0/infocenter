import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Database Configuration
DATABASE_URL = "postgresql://postgres:@localhost/budget_bloomberg"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# JWT Configuration
SECRET_KEY = "KWDS23w2asd02"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users_data"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

# Pydantic Schemas
class UserCreate(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Create the database tables
Base.metadata.create_all(bind=engine)

# Helper Functions
def get_user_by_email(db, email: str):
    logger.info(f"Fetching user with email: {email}")
    user = db.query(User).filter(User.email == email).first()
    if user:
        logger.info(f"User found: {user.email}")
    else:
        logger.warning(f"No user found with email: {email}")
    return user

def create_user(db, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    logger.info(f"Creating user: {user.email}, Hashed password: {hashed_password}")
    db_user = User(
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User created successfully: {db_user.email}")
    return db_user

def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if user:
        logger.info(f"Authenticating user: {email}")
        try:
            if pwd_context.verify(password, user.password):
                logger.info(f"Password verification successful for user: {email}")
                return user
            else:
                logger.warning(f"Password verification failed for user: {email}")
        except Exception as e:
            logger.error(f"Error during password verification for user: {email}: {str(e)}")
    return None

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.info(f"Token created for data: {data}")
    return token

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def register(user: UserCreate, db: SessionLocal = Depends(get_db)):
    logger.info(f"Registering user: {user.email}")
    db_user = get_user_by_email(db, user.email)
    if db_user:
        logger.warning(f"Email already registered: {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    logger.info(f"Login attempt for email: {form_data.username}")
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        logger.warning(f"Incorrect email or password for: {form_data.username}")
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    logger.info(f"Access token generated for user: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}

def read_users_me(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    logger.info("Decoding token for user retrieval")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            logger.warning("Invalid token: Missing subject")
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user_by_email(db, email)
        if user is None:
            logger.warning(f"User not found for email in token: {email}")
            raise HTTPException(status_code=401, detail="User not found")
        logger.info(f"User retrieved successfully: {user.email}")
        return user
    except JWTError as e:
        logger.error(f"JWT decode error: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid token")
