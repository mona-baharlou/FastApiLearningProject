from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)

server = "localhost"
database = "BlogDB"
driver = "ODBC Driver 17 for SQL Server"
sqlserver_url = (
    f"mssql+pyodbc://@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}&trusted_connection=yes"
)


# sqlserver_url = (f"mssql+pyodbc://@{server}/{database}?driver={
# driver.replace(' ', '+')}&trusted_connection=yes")


engine = create_engine(sqlserver_url)


# with engine.connect() as conn:
# result = conn.execute(text("SELECT SYSTEM_USER, GETDATE();"))
# for row in result:
# print("Connected as:", row[0], "| Time:", row[1])


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


