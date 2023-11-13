import pandas as pd
import requests

def download_stations():
    document = requests.get(
        "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt"
    ).text.split("\n")
    return document

def parse_stations(document):
    stations = []
    for line in document:
        stations.append(
            [
                line[:11],
                line[12:20],
                line[21:30],
                line[31:37],
                line[38:40],
                line[41:71],
                line[72:75],
                line[76:79],
                line[80:],
            ]
        )
    df_stations = pd.DataFrame(
        stations,
        columns=[
            "ID",
            "LATITUDE",
            "LONGITUDE",
            "ELEVATION",
            "STATE",
            "NAME",
            "GSN FLAG",
            "HCN/CRN FLAG",
            "WMO ID",
        ],
    )
    for col in df_stations.columns:
        df_stations[col] = df_stations[col].str.strip()

    # There is a row with only empty strings as values -> remove
    df_stations = df_stations[df_stations.ID != ""]
    df_stations = df_stations.astype({"LATITUDE":float, "LONGITUDE":float, "ELEVATION":float})
    return df_stations

def download_dly(station):
    download_url = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/all/"
    lines = []
    with requests.get(download_url + station + ".dly") as file:
        for line in file:
            lines.append(line.decode())
    lines = "".join(lines).split("\n")
    return lines

def parse_dly(document):

    string_split = [11, 15, 17, 21]
    for i in range(1,32):
        string_split_end = string_split[-1]
        string_split.append(string_split_end + 5)
        string_split.append(string_split_end + 6)
        string_split.append(string_split_end + 7)
        string_split.append(string_split_end + 8)

    station_col_names = ["ID","YEAR","MONTH","ELEMENT"]
    for i in range(1,32):
        station_col_names.append("VALUE" + str(i))
        station_col_names.append("MFLAG" + str(i))
        station_col_names.append("QFLAG" + str(i))
        station_col_names.append("SFLAG" + str(i))

    rows = []
    for line in document:
        vals = []
        last_end = 0
        for end in string_split:
            vals.append(line[last_end:end].strip())
            last_end = end
        rows.append(vals)
    df_station = pd.DataFrame(rows, columns=station_col_names)
    return df_station

def write_csv(df, path):
    df.to_csv(path)

def write_sql(df):
    pass

# Download and parse station data
stations = download_stations()
df_stations = parse_stations(stations)

# get us stations
df_stations_relevant = df_stations[df_stations.ID.str.startswith("US")]
relevant_stations = df_stations_relevant.ID

for station in relevant_stations:
    station_file = download_dly(station)

