# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://localhost/cyberdb"

engine = create_engine(DATABASE_URL)