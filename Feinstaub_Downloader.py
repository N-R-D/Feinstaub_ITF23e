import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from urllib.request import urlretrieve
from urllib.error import HTTPError
from os import path, makedirs
from datetime import date
from calendar import isleap
import tkcalendar as cal


def print_sensor_types(sensor_typen):
    for s in range(0, len(sensor_typen)):
        if s % 7 == 0 and s != 0:
            print(f"{sensor_typen[s]:<7}")
        else:
            print(f"{sensor_typen[s]:<7}", end=" ")


def generate_url(j, start_datum, end_datum, sensor_typ, sensor_id, mypath, url):
    current_date = date.today()
    start_tag, start_monat, start_jahr = map(int, start_datum.split("/"))
    end_tag, end_monat, end_jahr = map(int, end_datum.split("/"))
    monat_start = start_monat if j == start_jahr else 1  # hilfsvariable falls endmonat kleiner als startmonat
    monat_ende = end_monat if j == end_jahr else 12
    for m in range(monat_start, monat_ende + 1):
        days_in_month = 30 if m in [4, 6, 9, 11] else 29 if m == 2 and isleap(j) else 28 if m == 2 else 31
        start_tag = 1 if m != start_monat else start_tag
        end_tag = days_in_month if m != end_monat else end_tag
        for t in range(start_tag, end_tag + 1):
            if 2014 < j < 2022:
                date_url = f"{j:04d}-{m:02d}-{t:02d}"
                sensor_url = f"_{sensor_typ}_sensor_{sensor_id}"
                gesamt_url = f"{url}{j}/{date_url}/{date_url}{sensor_url}.csv.gz"
                print(gesamt_url)
                dateibenennung = path.join(f"{mypath}\\{j}\\{date_url}{sensor_url}.csv.gz")
                if not path.exists(dateibenennung):
                    try:
                        urlretrieve(gesamt_url, dateibenennung)
                    except HTTPError:
                        print(f"error 404: {gesamt_url}  konnte nicht gefunden werden")
                else:
                    continue
            elif j == 2022:
                if m < 7:
                    date_url = f"{j:04d}-{m:02d}-{t:02d}"
                    sensor_url = f"_{sensor_typ}_sensor_{sensor_id}"
                    gesamt_url = f"{url}{j}/{date_url}/{date_url}{sensor_url}.csv.gz"
                    print(gesamt_url)
                    dateibenennung = path.join(f"{mypath}\\{j}\\{date_url}{sensor_url}.csv.gz")
                    if not path.exists(dateibenennung):
                        try:
                            urlretrieve(gesamt_url, dateibenennung)
                        except HTTPError:
                            print(f"error 404: {gesamt_url}  konnte nicht gefunden werden")
                    else:
                        continue
                else:
                    date_url = f"{j:04d}-{m:02d}-{t:02d}"
                    sensor_url = f"_{sensor_typ}_sensor_{sensor_id}"
                    gesamt_url = f"{url}{j}/{date_url}/{date_url}{sensor_url}.csv"
                    print(gesamt_url)
                    dateibenennung = path.join(f"{mypath}\\{j}\\{date_url}{sensor_url}.csv")
                    if not path.exists(dateibenennung):
                        try:
                            urlretrieve(gesamt_url, dateibenennung)
                        except HTTPError:
                            print(f"error 404: {gesamt_url}  konnte nicht gefunden werden")
                    else:
                        continue
            elif j == current_date.year and m == current_date.month and t == current_date.day:
                exit(print(f"Das aktuelle Datum {current_date} ist erreicht alle weiteren Daten würden in der Zukunft liegen."))
            else:
                date_url = f"{j:04d}-{m:02d}-{t:02d}"
                sensor_url = f"_{sensor_typ}_sensor_{sensor_id}"
                gesamt_url = f"{url}/{date_url}/{date_url}{sensor_url}.csv"
                print(gesamt_url)
                dateibenennung = path.join(f"{mypath}\\{j}\\{date_url}{sensor_url}.csv")
                if not path.exists(dateibenennung):
                    try:
                        urlretrieve(gesamt_url, dateibenennung)
                    except HTTPError:
                        print(f"error 404: {gesamt_url}  konnte nicht gefunden werden")
                else:
                    continue


def url_generator(start_datum, end_datum, sensor_typ, sensor_id):
    heute = date.today()
    print(f"Dieses Programm erstellt und führt Download-URLs der Datenbank https://archive.sensor.community/  und ist gültig von 2015 bis {heute.year}")
    if end_datum is None or end_datum == "":
        end_datum = start_datum
    start_tag, start_monat, start_jahr = map(int, start_datum.split("/"))
    end_tag, end_monat, end_jahr = map(int, end_datum.split("/"))
    if not path.exists("Downloads"):
        makedirs("Downloads")
    mypath = "Downloads"

    if start_jahr > end_jahr:
        messagebox.showerror("Fehler", "Endjahr darf nicht kleiner als Startjahr sein")
        return
    elif 2014 < start_jahr <= heute.year or 2014 < end_jahr <= heute.year:
        url = "https://archive.sensor.community/"

        for j in range(start_jahr, end_jahr + 1):
            ordnerpfad = path.join(mypath, str(j))
            if not path.exists(ordnerpfad):
                makedirs(ordnerpfad)

            if start_jahr == end_jahr and start_monat > end_monat:
                messagebox.showerror("Fehler", "Der Startmonat darf nicht größer sein als der Endmonat innerhalb eines Jahres")
                return
            else:
                generate_url(j, start_datum, end_datum, sensor_typ, sensor_id, mypath, url)
    else:
        messagebox.showerror("Fehler", "Bitte gib ein gültiges Jahr an")
        return


def download_data():
    start_datum = start_date_calendar.get_date()
    end_datum = end_date_calendar.get_date()
    sensor_typ = sensor_type_combobox.get()
    sensor_id = sensor_id_entry.get()

    url_generator(start_datum, end_datum, sensor_typ, sensor_id)


root = tk.Tk()
root.title("Sensor Data Downloader")

infotext = ttk.Label(root, text=f"Dieses Programm ermöglicht den Download aus der Datenbank https://archive.sensor.community/ \ngültig von 2015 bis {date.today().year}")
infotext.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

start_date_label = ttk.Label(root, text="Startdatum:")
start_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

end_date_label = ttk.Label(root, text="Enddatum:")
end_date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

sensor_type_label = ttk.Label(root, text="Sensor Typ:")
sensor_type_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

sensor_id_label = ttk.Label(root, text="Sensor ID:")
sensor_id_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

start_date_calendar = cal.Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy")
start_date_calendar.grid(row=1, column=1, padx=5, pady=5)

end_date_calendar = cal.Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy")
end_date_calendar.grid(row=2, column=1, padx=5, pady=5)

sensor_type_combobox = ttk.Combobox(root, values=["bme280", "bmp180", "bmp280", "dht22", "ds18b20", "hpm", "htu21d",
                                                  "laerm", "pms1003", "pms3003", "pms5003", "pms6003", "pms7003", "ppd42ns",
                                                  "sds011", "sht11", "sht15", "sht30", "sht31", "sht35", "sht85", "sps30"])
sensor_type_combobox.grid(row=4, column=1, padx=5, pady=5)
sensor_type_combobox.current(0)

sensor_id_entry = ttk.Entry(root)
sensor_id_entry.grid(row=3, column=1, padx=5, pady=5)

download_button = ttk.Button(root, text="Download now", command=download_data)
download_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
