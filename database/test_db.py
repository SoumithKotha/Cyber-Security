# pyrefly: ignore [missing-import]
from sqlalchemy import text
from database.db import engine

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT version();")
    )

    print(result.fetchone())