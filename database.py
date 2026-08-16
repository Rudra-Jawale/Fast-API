from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Use SQLite as a fallback database (no external dependency required)
# Change to PostgreSQL when database is ready
db_url = "sqlite:///./telusko.db"
engine = create_engine(
    db_url,
    connect_args={"check_same_thread": False} if "sqlite" in db_url else {},
    poolclass=StaticPool if "sqlite" in db_url else None,
)
Session = sessionmaker(autocommit = False, autoflush= False, bind=engine)