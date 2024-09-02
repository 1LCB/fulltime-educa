from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.config import get_environment_variables

env = get_environment_variables()


class ConnectionHandler:
    def __init__(self):
        self.db_url = f"mysql+pymysql://{env.ENV_MYSQL_USER}:{env.ENV_MYSQL_PASS}@{env.ENV_MYSQL_HOST}:{env.ENV_MYSQL_PORT}/{env.ENV_MYSQL_BASE}"
        self.engine = None
        self.Session = None

    def __enter__(self):
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)
        return self.Session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.Session is not None:
            self.Session.close_all()
        if self.engine is not None:
            self.engine.dispose()
