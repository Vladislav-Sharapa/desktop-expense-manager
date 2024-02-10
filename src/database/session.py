from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True
) 
Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session

# @contextmanager
# def ssession_scope():
#     session = Session()  # def __enter__
#     try:
#         yield session  #Pass session with as
#         session.commit()  #If nothing happens, commit()
#     except:
#         session.rollback()  #Rollback if error occurs()
#         raise
#     finally:
#         session.close()  #Either way, it will eventually close()


# def session_scope(func):
#     def wrapper(self, *args, **kwargs):
#         session = Session()
#         try:
#             result = func(self, session, *args, **kwargs)
#             session.commit()
#             return result
#         except Exception as e:
#             session.rollback()
#             raise
#         finally:
#             session.close()
#     return wrapper

def session_scope(commit_required: bool = True):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            session = Session()
            try:
                result = func(self, session, *args, **kwargs)
                if commit_required:
                    session.commit()
                return result
            except Exception as e:
                session.rollback()
                raise
            finally:
                session.close()
        return wrapper
    return decorator