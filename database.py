from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///./tagz.db"
engine = create_engine(DATABASE_URL)

# Create the tables defined in your models
Base.metadata.create_all(bind=engine)

# Create a sessionmaker to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
