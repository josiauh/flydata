from flydata import uri

data = uri.plainURI("Yo dude!")

print(data)

print(uri.readURI(data))

data = uri.fileToURI(__file__, "application/x-python-code")

print(data)