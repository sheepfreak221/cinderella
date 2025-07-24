#!/usr/bin/python
# -*- coding: utf-8 -*-

import fileinput, string, sys, os, shutil

MENU_PFAD = "./input/menu.txt"

# Prüfe, ob ein Menü vorhanden ist und lese es ein
	
try:
	menu = open(MENU_PFAD).read()
except:
	print("Error: No menu was found")
	sys.exit(0)	

#Lese das Verzeichnis ein 

try:
	verzeichnisinhalt = os.listdir("./templates")
except:
	print("Error: The directory can't be read")
	sys.exit(0)	

for html_datei in verzeichnisinhalt:

#Kopiere die Datei
 
	shutil.copyfile("./templates/" + html_datei, "./output/" + html_datei)

#Verändere den Inhalt

	for line in fileinput.input("./output/" + html_datei,inplace=1):
     		line = line.replace("<!--MENU-->", menu)
     		sys.stdout.write(line)


