import csv

TIME_POS = 0
OCCUPANT_NUM_POS = 1
INDOOR_AMBIENT_TEMP_POS = 5
INDOOR_RELATIVE_HUMIDITY_POS = 6
INDOOR_AIR_VELOCITY_POS = 7
INDOOR_MEAN_RADIANT_TEMP_POS = 8
PMV_POS = 117
NOT_NUMBER = "NaN"
column_data = {"time" : TIME_POS, "occupant_num" : OCCUPANT_NUM_POS, "indoor_ambient_temp" : INDOOR_AMBIENT_TEMP_POS,
          "indoor_relative_humidity" : INDOOR_RELATIVE_HUMIDITY_POS, "indoor_air_velocity" : INDOOR_AIR_VELOCITY_POS,
         "indoor_mean_radiant_temp" : INDOOR_MEAN_RADIANT_TEMP_POS, "pmv" : PMV_POS}


def str_to_float(string):
    if string == NOT_NUMBER:
        return 0.0;
    return float(string)

def get_data(row):
    return {col_name: str_to_float(row[col_pos]) for col_name, col_pos in column_data.items()}

def read_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return [get_data(row) for row in csv_reader]
    return []

def write_file(data, file_name):
    with open(file_name, 'w') as csv_file:
        col_names = column_data.keys()
        csv_writer = csv.DictWriter(csv_file, col_names)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)