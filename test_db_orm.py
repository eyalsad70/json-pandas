import sqlalchemy as sqla
import sqlalchemy.orm as db
from create_my_engine import create_db_engine
from sqlalchemy.exc import IntegrityError

import pandas as pd

class Base(db.DeclarativeBase):
    '''SQLAlchemy forces using a common base class for all mapped classes.'''
    pass

class Player(Base):
    __tablename__ = "players_orm"
    
    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    Name: db.Mapped[str] = db.mapped_column(sqla.String(30), unique=True)
    YOB: db.Mapped[int] = db.mapped_column(sqla.Integer)
    Team: db.Mapped[str] = db.mapped_column(sqla.String(30))
    Goals: db.Mapped[int] = db.mapped_column(sqla.Integer)

    def __repr__(self) -> str:
        return f"Player(Name={self.Name}, YOB={self.YOB}, Team={self.Team}, Goals={self.Goals})"


def add_user_with_unique_constraint(new_player):
    with db.Session(engine) as session:
        session.add(new_player)
        try:
            session.commit()
            print("Player added.")
        except IntegrityError:
            session.rollback()  # Rollback the session in case of failure
            print("Player with this name already exists.")
        

def orm_create_add(engine):
    # Player.__table__.drop(engine) # delete table
    Player.metadata.create_all(engine)
    add_user_with_unique_constraint(Player(Name='Lionel Messi', YOB=1987, Team='Argentina', Goals=103))
    add_user_with_unique_constraint(Player(Name='Paul Pogba', YOB=1993, Team='France', Goals=11))
    add_user_with_unique_constraint(Player(Name='Cristiano Ronaldo', YOB=1985, Team='Portugal', Goals=123))
    # with db.Session(engine) as session:
    #     with session.begin():
    #         session.add_all([
    #             Player(Name='Lionel Messi', YOB=1987, Team='Argentina', Goals=103),
    #             Player(Name='Paul Pogba', YOB=1993, Team='France', Goals=11),
    #             Player(Name='Cristiano Ronaldo', YOB=1985, Team='Portugal', Goals=123)
    #         ])

def orm_select(engine):
    with db.Session(engine) as session:
        players = session.query(Player).all()
        for player in players:
            print(player)

            
if __name__ == '__main__':
    engine = create_db_engine()
    orm_create_add(engine)
    print("\n" * 5)
    # orm_select(engine)
    
    df = pd.read_sql_table(Player.__tablename__, engine)
    print(df)
    
    
