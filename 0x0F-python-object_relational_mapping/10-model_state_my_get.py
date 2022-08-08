#!/usr/bin/python3
"""lists all State objects from the database"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    name = sys.argv[4]
    states = session.query(State).filter(State.name.like(
        name)).first()
    if (states is None):
        print("Not found")
    else:
        print(states.id)
