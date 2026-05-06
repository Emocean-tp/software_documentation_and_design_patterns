from datetime import datetime

from models import Customer, Car, Rental
from dal import IRepository, IFileLoader


class RentalImportService:

    def __init__(self, repo: IRepository, loader: IFileLoader):
        self.repo = repo
        self.loader = loader

    def process_data(self, file_path):

        rows = self.loader.load_csv(file_path)

        customers = {}
        cars = {}

        for row in rows:

            email = row['customer_email']

            if email not in customers:

                customer = Customer(
                    firstName=row['customer_first_name'],
                    lastName=row['customer_last_name'],
                    email=email
                )

                customers[email] = customer
                self.repo.add(customer)

            car_key = f"{row['car_brand']}_{row['car_model']}"

            if car_key not in cars:

                car = Car(
                    brand=row['car_brand'],
                    model=row['car_model'],
                    year=int(row['car_year']),
                    pricePerDay=float(row['price_per_day'])
                )

                cars[car_key] = car
                self.repo.add(car)

            rental = Rental(
                customer=customers[email],
                car=cars[car_key],

                startDate=datetime.strptime(
                    row['start_date'],
                    "%Y-%m-%d"
                ).date(),

                endDate=datetime.strptime(
                    row['end_date'],
                    "%Y-%m-%d"
                ).date(),

                totalPrice=float(row['total_price'])
            )

            self.repo.add(rental)

        self.repo.commit()