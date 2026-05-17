from sqlalchemy import create_engine

DATABASE_URL = "postgresql://admin:password@localhost/frauddb"

engine = create_engine(DATABASE_URL)