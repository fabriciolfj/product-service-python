import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class UnitWork:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        db_url = config['database']['url']
        self.session = Session(create_engine(db_url))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()


    def __enter__(self):
        return self
