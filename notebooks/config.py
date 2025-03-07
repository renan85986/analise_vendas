from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "papai2010"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "analisevendas"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
