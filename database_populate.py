from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Item, Base

engine = create_engine('sqlite:///sportinggoodscatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create categories
session.add(Category(name="Baseball"))
session.commit()

session.add(Category(name="Football"))
session.commit()

session.add(Category(name="Basketball"))
session.commit()

session.add(Category(name="Hockey"))
session.commit()

session.add(Category(name="Tennis"))
session.commit()
