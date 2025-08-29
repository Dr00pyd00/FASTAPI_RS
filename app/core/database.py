from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = 'sqlite:///./database.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base pour les tables :
Base = declarative_base()


# fonction qui va me donner la db puis la fermer avec Depends:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        
        
