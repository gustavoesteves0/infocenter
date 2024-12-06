from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative
import logging

# Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Database Configuration
DATABASE_URL = "postgresql://postgres:@localhost/budget_bloomberg"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Base for SQLAlchemy models
@as_declarative()
class Base:
    pass

# Dependency for getting a database session
def get_db():
    """Provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Database Initialization Function
def initialize_database():
    from app.models import auth # Let the database aware of the models
    logger.info("Initializing database and creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
