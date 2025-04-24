import csv
import pickle

class PickleSerializerMixin:
    @staticmethod
    def write_pickle(data: list[dict[str, any]], filename: str):
        with open(filename, "wb") as fh:
            pickle.dump(data, fh)
            
    @staticmethod
    def read_pickle(filename: str):
        with open(filename, "rb") as fh:
            return pickle.load(fh)
        
class CsvSerializerMixin:
    @staticmethod
    def write_csv(data: list[dict[str, any]], filename: str):
        """Save to CSV"""
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def read_csv(filename: str) -> list[dict[str, any]]:
        """Load from CSV"""
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
class Serializer(CsvSerializerMixin, PickleSerializerMixin):
    pass