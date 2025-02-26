# Classes for processing records

class RecordProcessor:
    def __init__(self):
        pass

    

class Record:
    def __init__(self):
        self.data_points = []

    def parse(self):
        pass




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