# Classes for processing records

class Record:
    def __init__(self, header, record):
        self.record = record
        self.header = header
        self.data_points = self.parse(self.record)

    def parse(self):
        print("Parsing record...")

    def get_value_from_key(self, key):
        return self.data_points[key]


class HeaderRecord(Record):
    pass

class DataRecord(Record):
    pass

class DataPoint:
    def __init__(self):
        pass

    def validate(self):
        pass

    def transform(self):
        pass

    def clean(self):
        pass