import csv, json
import datetime

def read_csv(csv_path):
    columns = []
    data = []

    def format_column(column, item):
        if item == "":
            return None
        if column in ["updated", "tenderDate", "periodStartDate", "periodEndDate", "tenderSubmissionDeadline", "awardDate"]:
            return datetime.datetime.fromisoformat(item)
        if column in ["periodDurationInDays", "lot", "numberOfTenderers"]:
            return int(item)
        if column in ["valueAmount", "awardValueAmount"]:
            return float(item)
        if column in ["contactPoint_faxNumber", "contactPoint_telephone"]:
            return item[:9]
        if column in ["municipio_id", "postal_code"]:
            return item[:5]
        return str(item)

    try:
        with open(csv_path, newline='', encoding="utf-8-sig") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for counter, row in enumerate(spamreader):
                item = {}
                for i, field in enumerate(row):
                    if counter == 0:
                        columns.append(field)
                    else:
                        item[columns[i]] = format_column(columns[i], field)
                data.append(item)
    except Exception as e:
        print(e)

    return data

def print_parsed(data):
    parsed_data = json.dumps(data, indent=4, default=str)
    print(parsed_data)