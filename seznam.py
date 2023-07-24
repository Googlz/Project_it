from zakaznik import Zakaznik

class Seznam:

	def __init__(self):
		self.seznam_pojisteni = []

	def pridat_pojistenec(self):
		jmeno = input("Zadejte jméno pojištěného:")
		prijmeni = input("Zadejte příjmení pojištěného:")
		telefon = input("Zadejte telefonní číslo pojištěného:")
		vek = input("Zadejte věk pojištěného:")

		# vytvoření instance
		novy_pojistenec = Zakaznik(jmeno, prijmeni, telefon, vek)
		self.seznam_pojisteni.append(novy_pojistenec)
		print(f"Přidali jste nového zákazníka  {novy_pojistenec}")

	def vypis_pojistence(self):
		for pojistenci in self.seznam_pojisteni:
			print(pojistenci)

	def vyhledani_pojistence(self):
		jmeno = input("Zadejte jméno pojištěného:")
		prijmeni = input("Zadejte příjmení pojištěného:")

		vyhledani = None
		for pojistenec in self.seznam_pojisteni:
			if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
				vyhledani = pojistenec
				break

		if vyhledani:
			print("Nalezený pojištěnec:")
			print(f"Jméno: {vyhledani.jmeno}, příjmení: {vyhledani.prijmeni}, telefon: {vyhledani.telefon}, věk: {vyhledani.vek}")
		else:
			print("Pojištěnec nenalezen.")