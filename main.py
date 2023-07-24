from seznam import Seznam

evidence = Seznam()

while True:
	print("Evidence pojištěných")
	print("1 - Přidat nového pojištěného")
	print("2 - Vypsat všechny pojištěné")
	print("3 - Vyhledat pojištěného")
	print("4 - Konec")

	volba = input()

	if (volba == "1"):
		evidence.pridat_pojistenec()

	elif (volba == "2"):
		evidence.vypis_pojistence()
	elif (volba == "3"):
		evidence.vyhledani_pojistence()
	elif (volba =="4"):
		break