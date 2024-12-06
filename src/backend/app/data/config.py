from sqlalchemy import create_engine, Column, Integer, Float, String, Date, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
DATABASE_URL = "postgresql://postgres:password@localhost/economic_data"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Table Definitions
class GDP(Base):
    __tablename__ = "gdp_data"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    realGDP = Column(Float)
    gdp = Column(Float)
    realgdpgrowthrate = Column(Float)
    yoy = Column(Float)

class CPI(Base):
    __tablename__ = "cpi_data"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    value = Column(Float)
    mom = Column(Float)
    yoy = Column(Float)

class Fed_Funds_Rate(Base):
    __tablename__ = 'ffr_data'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    effr = Column(Float)
    ffrul = Column(Float)
    ffrll = Column(Float)
    effravgc = Column(Float)

class JOLTS(Base):
    __tablename__ = 'jolts_data'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    value = Column(Float)
    mom = Column(Float)
    yoy = Column(Float)

class Payroll(Base):
    __tablename__ = 'payroll_data'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    value = Column(Float)
    mom = Column(Float)
    yoy = Column(Float)

# Initialize Database
def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    initialize_database()
