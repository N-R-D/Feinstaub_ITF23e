# Feinstaub_ITF23e
Feinstaub Downloader &amp; Datenanalyse


Diese READ ME Datei wird eine erklärung über die programme URL_Download.py & CSV_Analyse.py bieten.


URL-Download.py

Beim ausführen der Datei wird eine Grafische benutzerfläche erscheinen welche folgendes enthält:

2 Kalender 
	einen für die Auswahl des start Datums
	einen für die Auswahl des end Datums

ein Dropdown menü
	welches eine Auswahl der Sensortypen bietet

ein Entryfeld 
	welches die Eingabe der SensorID erwartet
	dht22  = 3660
	sds011 = 3659

einen Button
	welchen den Download startet.

Gespeichert werden die CSV dateien dann in Jährliche unterordner, welche im Selben ordner erstellt werden in dem sich Das programm befindet.


CSV_Analyse.py

Nach dem Ausführen wird eine Grafische Benutzeroberfläche Dargestellt, welches folgende Elemente enthält:

einen Kalendar zur Auswahl des Datums, der Datei welche angezeigt werden soll

2 Button
	Ein button welcher ein Hilfe fenster öffnet
	Ein button welcher das Grafische darstellen der Daten initialisiert.

die grafische Darstellung enthält

2 Graphen 
	ein graph für die PM2.5 Werte
	ein graph für die PM10 Werte

die Achsen bezeichnung ist 
	x-achse: Zeit im format HH:MM von 00:00 bis 24:00
	y-achse Links : Die konzentration in µg/m³
	y-achse Rechs : Minimal-, Durchschnitts & Maximalwerte 

desweiteren gibt es 2 Grids
	ein grid welches die Ticks der x & y-achse Links zusammenführt
	ein grid welches eine Grade linie an den stellen zieht wo sich die Minimal-, Durchschnitts & Maximalwerte befinden



CSV_analyse.py greift auf die von URL_Download.py gespeicherten dateien zu. Also ist es Ratsam, CSV_Analyse.py erst auszuführen nachdem URL_Download.py Daten gespeichert hat.
