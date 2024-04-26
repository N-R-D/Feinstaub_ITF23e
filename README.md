# Feinstaub_ITF23e
Feinstaub Downloader &amp; Datenanalyse


Diese READ ME Datei wird eine erklärung über die programme Feinstaub_Downloader.py & Feinstaub_Datenanalyse.py bieten.

Feinstaub_Datenanalyse.py greift auf die von Feinstaub_Downloaderpy gespeicherten Dateien zu
Also ist es Ratsam, Feinstaub_Downloader.py zu erst auszuführen und danach erst Feinstaub_Datenanalyse.py 

Feinstaub_Downloader.py

Beim ausführen der Datei wird eine Grafische benutzerfläche erscheinen welche folgendes enthält:

2 Kalender 
	
 einen für die Auswahl des start Datums
	
 einen für die Auswahl des end Datums

ein Dropdown menü
	
 welches eine Auswahl der Sensortypen bietet

ein Entryfeld 
	welches die Eingabe der SensorID erwartet:
	
 dht22  = 3660  - für den Temperatur- , Luftdruck- & Feuchtigkeitssensor der TBS1
	
 sds011 = 3659	- für den Feinstaubsensor der TBS1

 Jedoch können mit diesem Programm jegliche Daten des https://archive.sensor.community/ Archieves

einen Button
	welchen den Download startet.

Gespeichert werden die CSV dateien dann in Jährliche unterordner, welche im Selben ordner erstellt werden in dem sich Das programm befindet.


Feinstaub_Datenanalyse.py

Nach dem Ausführen wird eine Grafische Benutzeroberfläche Dargestellt, welches folgende Elemente enthält:

einen Kalendar zur Auswahl des Datums, der Datei welche angezeigt werden soll

2 Button:

Ein button welcher ein Hilfe fenster öffnet

Ein button welcher das Grafische darstellen der Daten initialisiert.


die grafische Darstellung enthält

2 Graphen 
	
 ein graph für die PM2.5 Werte
	
 ein graph für die PM10 Werte

die Achsen bezeichnung ist:

x-achse: Zeit im format HH:MM von 00:00 bis 24:00
 
y-achse Links : Die konzentration in µg/m³
 
y-achse Rechs : Minimal-, Durchschnitts & Maximalwerte
 

desweiteren gibt es 2 Grids
	
ein grid welches die Ticks der x & y-achse Links zusammenführt
	
ein grid welches eine Grade linie an den stellen zieht wo sich die Minimal-, Durchschnitts & Maximalwerte befinden




