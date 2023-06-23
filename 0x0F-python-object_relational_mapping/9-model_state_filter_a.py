#!/usr/bin/python3
""" Prints all states with letter a in there name """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Check if all arguments are provided """
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    states_a = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()

    for states in states_a:
        print('{0}: {1}'.format(states.id, states.name))
