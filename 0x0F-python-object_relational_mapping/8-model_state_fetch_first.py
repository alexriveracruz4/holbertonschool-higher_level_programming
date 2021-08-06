#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    first_st = session.query(State).order_by(State.id).first()
    if first_st is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_st.id, first_st.name))
    session.close()
