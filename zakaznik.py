class Zakaznik:

	def __init__(self, jmeno, prijmeni, telefon, vek):
		self.jmeno = jmeno
		self.prijmeni = prijmeni
		self.telefon = telefon
		self.vek = vek


	def __str__(self):
		return f"Jméno: {self.jmeno}, příjmení: {self.prijmeni}, telefon: {self.telefon}, věk {self.vek}"
