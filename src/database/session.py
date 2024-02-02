from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True
) 
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()  # def __enter__
    try:
        yield session  #Pass session with as
        session.commit()  #If nothing happens, commit()
    except:
        session.rollback()  #Rollback if error occurs()
        raise
    finally:
        session.close()  #Either way, it will eventually close()