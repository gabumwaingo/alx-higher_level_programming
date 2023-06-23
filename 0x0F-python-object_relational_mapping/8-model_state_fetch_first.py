#!/usr/bin/python3
""" Prints the first state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Check if all arguments are provided """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(          sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State).first()

    if first_state:
        print("1: {}".format(first_state.name))
    else:
        print("No states found in the table.")
