import csv
import pickle

class PickleSerializerMixin:
    @staticmethod
    def write_pickle(data, filename):
        """Save using pickle"""
        try:
            with open(filename, "wb") as fh:
                pickle.dump(data, fh)                
        except pickle.PicklingError:
            print("Pickling failed")
            
    @staticmethod
    def read_pickle(filename):
        """Load using pickle"""
        try:
            with open(filename, "rb") as fh:
                return pickle.load(fh)
        except pickle.UnpicklingError:
            print("Unpickling failed")
        
class CsvSerializerMixin:
    @staticmethod
    def write_csv(data, filename):
        """Save to CSV"""
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except csv.Error:
            print("Csv write failed")

    @staticmethod
    def read_csv(filename):
        """Load from CSV"""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except csv.Error:
            print("Csv read failed")
            
class Serializer(CsvSerializerMixin, PickleSerializerMixin):
    pass