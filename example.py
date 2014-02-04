# First, import lolo
import abbrev

# Define your web app
class ExampleApp(abbrev.Form):
	def __init__(self):
		self.name =	abbrev.Fields.text("Name", required = True)
		self.password = abbrev.Fields.password("Password", required = True)
		self.address = abbrev.Fields.password("Address")
		
# Run it!
ExampleApp.run()