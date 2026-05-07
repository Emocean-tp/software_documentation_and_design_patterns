from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from dal import SqlAlchemyRepository, CsvLoader
from bll import MovieImportService


def main():

    engine = create_engine('sqlite:///app.db')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    repo = SqlAlchemyRepository(session)
    loader = CsvLoader()

    service = MovieImportService(repo, loader)

    print("Starting IMDB import...")

    service.process_data("data.csv")

    print("IMDB import completed!")


if __name__ == "__main__":
    main()