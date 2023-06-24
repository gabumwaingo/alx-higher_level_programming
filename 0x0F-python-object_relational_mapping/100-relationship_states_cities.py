#!/usr/bin/python3
""" Creates the state califonia with sanfrancisco """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """ Check if all arguments are provided """
    if len(sys.argv) != 4:
        print("Usage: python3 100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    # Create the State "California" with the City "San Francisco"
    california = State(name='California', cities=[City(name='San Francisco')])

    session.add(california)
    session.commit()

    session.close()

