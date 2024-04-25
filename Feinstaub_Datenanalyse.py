import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from os import path
import csv
import gzip
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar


def load_data(start_calendar):
    """Einlesen der CSV dateien"""
    mypath = "Downloads"
    start_datum = start_calendar.get_date()
    sensor_typ = "sds011"
    sensor_id = "3659"
    start_tag, start_monat, start_jahr = map(int, start_datum.split("/"))
    sensor_url = f"_{sensor_typ}_sensor_{sensor_id}"

    if start_jahr <= 2022:
        csv_datenpfad_gz = path.join(
            f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}{sensor_url}.csv.gz")
        csv_datenpfad = path.join(
            f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}{sensor_url}.csv")
        input_file = csv_datenpfad_gz
        output_file = csv_datenpfad
        if not path.exists(csv_datenpfad_gz):
            messagebox.showinfo("Info", "Keine Daten gefunden.")
            return None
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        with open(csv_datenpfad, mode='r') as file:
            reader = csv.DictReader(file, delimiter=";")
            data = list(reader)
    else:
        csv_datenpfad = path.join(
            f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}{sensor_url}.csv")
        if not path.exists(csv_datenpfad):
            messagebox.showinfo("Info", "Keine Daten gefunden.")
            return None
        with open(csv_datenpfad, mode='r') as file:
            reader = csv.DictReader(file, delimiter=";")
            data = list(reader)
    plot_data(data, start_datum)
    return data


def plot_data(data, start_datum):
    """Daten in einem Plot zusammenführen und Anzeigen"""
    column = list(data[0].keys())
    time_reverse = [x for x in range(0, 1441)]
    x = time_conversion(data)
    y1 = [float(row[column[6]]) for row in data]
    y2 = [float(row[column[9]]) for row in data]
    min_value_1 = min(y1)
    max_value_1 = max(y1)
    med_value_1 = sum(y1) / len(y1)

    min_value_2 = min(y2)
    max_value_2 = max(y2)
    med_value_2 = sum(y2) / len(y2)

    fig, ax = plt.subplots(1, 2, figsize=(14, 7), sharey=False, facecolor="#AB82FF")
    plt.subplots_adjust(wspace=0.35)

    ax[0].plot(x, y1, color='black', linestyle='solid', linewidth=1.5)
    ax[0].set_xlabel('Tageszeit')
    ax[0].set_ylabel(f"10µm  Partikelkonzentration in μg/m³")
    ax[0].set_title(f"10µm Partikelgröße für den {start_datum}")
    ax[0].set_ylim(int(min_value_1-1), int(max_value_1+2))
    ax[0].set_yticks([i for i in range(int(min_value_1), int(max_value_1) + 2)])
    ax[0].set_xticks(time_reverse)
    ax[0].set_xticklabels(["{:02d}:{:02d}".format(x // 60, x % 60) for x in time_reverse], fontsize=10, rotation=45)
    ax[0].grid(True, linewidth=.75, color="#AAAAAA", linestyle="solid")
    ax[0].yaxis.set_major_locator(MaxNLocator(nbins=25))
    ax[0].xaxis.set_major_locator(MaxNLocator(nbins=24))

    ax[1].plot(x, y2, color='black', linestyle='solid', linewidth=1.5)
    ax[1].set_xlabel('Tageszeit')
    ax[1].set_ylabel(f"2.5µm  Partikelkonzentration in μg/m³")
    ax[1].set_title(f"2.5µm Partikelgröße für den {start_datum}")
    ax[1].set_ylim(int(min_value_2 - 1), int(max_value_2 + 2))
    ax[1].set_yticks([i for i in range(int(min_value_2), int(max_value_2) + 2)])
    ax[1].set_xticks(time_reverse)
    ax[1].set_xticklabels(["{:02d}:{:02d}".format(x // 60, x % 60) for x in time_reverse], fontsize=10, rotation=45)
    ax[1].grid(True, linewidth=.75, color="#AAAAAA", linestyle="solid")
    ax[1].yaxis.set_major_locator(MaxNLocator(nbins=25))
    ax[1].xaxis.set_major_locator(MaxNLocator(nbins=24))

    ax2 = ax[0].twinx()
    ax2.plot([], [])
    ax2.set_ylabel("Min Durchschnitt Max Werte")
    ax2.set_ylim(int(min_value_1 - 1), int(max_value_1 + 2))
    ax2.set_yticks([round(min_value_1, 2), round(med_value_1, 2), round(max_value_1, 2)])
    ax2.grid(True, linewidth=1, color="#FF00CC")

    ax3 = ax[1].twinx()
    ax3.plot([], [])
    ax3.set_ylabel("Min Durchschnitt Max Werte")
    ax3.set_ylim(int(min_value_2 - 1), int(max_value_2) + 2)
    ax3.set_yticks([round(min_value_2, 2), round(med_value_2, 2), round(max_value_2, 2)])
    ax3.grid(True, linewidth=1, color="#FF00CC")

    plt.show()


def time_conversion(data):
    """Umwandlung des timestamps in minuten"""
    list_of_times = []
    for entry in data:
        dt = datetime.strptime(entry['timestamp'], "%Y-%m-%dT%H:%M:%S")
        hours = dt.hour
        minutes = dt.minute
        total_minutes = hours * 60 + minutes
        list_of_times.append(total_minutes)
    return list_of_times


sensor_typen = ["bme280", "bmp180", "bmp280", "dht22", "ds18b20", "hpm", "htu21d",
                "laerm", "pms1003", "pms3003", "pms5003", "pms6003", "pms7003", "ppd42ns",
                "sds011", "sht11", "sht15", "sht30", "sht31", "sht35", "sht85", "sps30"]


def get_selected_period(start_calendar):
    """zusammenführen der ausgewählten daten und einlesen der CSV Spalten namen"""
    start_date = start_calendar.get_date()
    start_tag, start_monat, start_jahr = map(int, start_date.split("/"))

    sensor_typ = "sds011"
    sensor_id = "3659"
    mypath = "Downloads"

    csv_columns = set()

    if start_jahr <= 2022:
        csv_datenpfad_gz = path.join(
            f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}_{sensor_typ}_sensor_{sensor_id}.csv.gz")
        csv_datenpfad = path.join(
            f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}_{sensor_typ}_sensor_{sensor_id}.csv")
        input_file = csv_datenpfad_gz
        output_file = csv_datenpfad

        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        with open(csv_datenpfad, 'r') as file:
            csv_reader = csv.reader(file, delimiter=";")
            column = next(csv_reader)
            csv_columns.update(column)
    else:
        csv_datenpfad = path.join(
           f"{mypath}/{start_jahr:04d}/{start_jahr:04d}-{start_monat:02d}-{start_tag:02d}_{sensor_typ}_sensor_{sensor_id}.csv")
        with open(csv_datenpfad, 'r') as file:
            csv_reader = csv.reader(file, delimiter=";")
            column = next(csv_reader)
            csv_columns.update(column)


def zeige_messagebox():
    messagebox = tk.Toplevel()
    messagebox.title("Hilfe")

    text = ("Dieses Programm zeigt die Daten von Partikelgröße 2,5µm und 10µm zugleich an.\n"
            "Alles was Sie dafür tun müssen ist, ein Datum auswählen und auf 'Ausgewähltes Datum Anzeigen' Drücken.\n"
            "Sollten Sie beim Betätigen eine Meldung 'Keine Daten gefunden' bekommen, wählen Sie bitte ein anderes Datum\n"
            "oder laden Sie die Daten mithilfe des beigelegten URL-Downloaders herunter.")

    label = tk.Label(messagebox, text=text, padx=10, pady=10)
    label.pack()

    ok_button = tk.Button(messagebox, text="OK", command=messagebox.destroy)
    ok_button.pack()

    read_me = tk.Button(messagebox, text="READ ME öffnen", command=lambda: open("READ_ME.txt"))
    read_me.pack()


def create_gui(root):
    """Diese Funktion erzeugt die benötigten elemente des GUIs  """
    start_label = tk.Label(root, text="Bitte wähle ein Datum aus.")
    start_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    start_calendar = Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy")
    start_calendar.grid(row=1, column=0, columnspan=2, padx=20, pady=15)

    plot_button = tk.Button(root, text="Ausgewähltes Datum Anzeigen", command=lambda: load_data(start_calendar))
    plot_button.grid(row=2, column=1, padx=5, pady=10)

    hilfe_button = tk.Button(root, text="Hilfe", command=zeige_messagebox)
    hilfe_button.grid(row=2, column=0, padx=5, pady=10)

    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Feinstaub Daten")
    create_gui(root)
