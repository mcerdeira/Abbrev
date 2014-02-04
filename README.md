Abbrev
======

Simplest web pages generator


Why?
====

I wan't to provide a really simplistic way of creating a web page


Example
=====

```python
# First, import abbrev
import abbrev

# Define your web app, as a class
class ExampleApp(abbrev.Form):
    def __init__(self):
        self.name = abbrev.Fields.text("Name", required = True)
        self.password = abbrev.Fields.password("Password", required = True)
        self.address = abbrev.Fields.password("Address")
	
# Run it!
ExampleApp.run()
```

That's it?
==========

Yes. You may think that this is crap, or stupid, but, the main idea is to provide a simple and quick way of creating web pages with basic interactions.
