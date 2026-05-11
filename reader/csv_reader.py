import csv

class CsvReader:
    def read(self, path):
        data = []
        with open(path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data