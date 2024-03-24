from sqlalchemy import create_engine
from config import DB_PASSWORD, DB_USER, DB_HOST, DB_PORT, DB_NAME

db_engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")