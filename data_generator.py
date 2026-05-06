import csv
import random

from datetime import datetime, timedelta


def generate_csv(filename="data.csv", rows=1050):

    headers = [
        "customer_first_name",
        "customer_last_name",
        "customer_email",
        "car_brand",
        "car_model",
        "car_year",
        "price_per_day",
        "start_date",
        "end_date",
        "total_price"
    ]

    brands = {
        "Toyota": ["Camry", "Corolla", "RAV4"],
        "BMW": ["X5", "320i", "M5"],
        "Audi": ["A4", "Q7", "A6"],
        "Mercedes": ["C-Class", "E-Class", "GLA"]
    }

    with open(filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        for i in range(rows):

            brand = random.choice(list(brands.keys()))
            model = random.choice(brands[brand])

            year = random.randint(2015, 2024)

            price_per_day = round(random.uniform(40, 300), 2)

            start = datetime.now().date() + timedelta(days=i)

            days = random.randint(1, 14)

            end = start + timedelta(days=days)

            total_price = round(price_per_day * days, 2)

            writer.writerow([
                f"Customer{i}",
                f"Surname{i}",
                f"user{i}@mail.com",
                brand,
                model,
                year,
                price_per_day,
                start,
                end,
                total_price
            ])

    print(f"CSV file '{filename}' created successfully with {rows} rows.")


if __name__ == "__main__":
    generate_csv()