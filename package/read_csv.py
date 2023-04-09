import csv


def read_csv(file):
    """Read a CSV file"""
    with open(file, 'r') as f:
        read = csv.reader(f, delimiter=",")
        header = next(read)
        data = []
        for line in read:
            information = list(zip(header, line))
            data.append({header: value for header, value in information})
        return data


def select_column(data, column):
   return [row[column] for row in data]
