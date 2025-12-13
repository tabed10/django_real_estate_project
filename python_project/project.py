class Person:
	def __init__(self, f_name: str, l_name: str):
		self.f_name = f_name
		self.l_name = l_name

	def get_full_name(self):
		return f"{self.f_name} {self.l_name}"

person = Person(f_name="Sabbir", l_name="Hossain")
print(person.get_full_name())

class Engineer(Person):
	def __init__(self, f_name: str, l_name: str, position: str):
		super().__init__(f_name=f_name, l_name=l_name)
		self.position = position

	def get_position(self):
		return f"SWE: {self.position}"

eng = Engineer(f_name="Sabbir", l_name="Hossain", position="L3")
print("name: ", eng.get_full_name(), "position: ", eng.get_position())
