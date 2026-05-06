from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from dal import SqlAlchemyRepository, CsvLoader
from bll import RentalImportService


def main():

    engine = create_engine('sqlite:///app.db')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    repo = SqlAlchemyRepository(session)

    loader = CsvLoader()

    service = RentalImportService(repo, loader)

    print("Starting import...")

    service.process_data("data.csv")

    print("Import completed!")


if __name__ == "__main__":
    main()