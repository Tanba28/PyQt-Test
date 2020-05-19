import argparse
import pandas as pd

from PyQt5 import QtCore

def transform_date(utc,timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QtCore.QDateTime().fromString(utc,utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date

def read_data(frame):
    df = pd.read_csv(frame)

    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    timezone = QtCore.QTimeZone(b"Europe/Berlin")

    times = df["time"].apply(lambda x: transform_date(x,timezone))

    return times,magnitudes

if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)