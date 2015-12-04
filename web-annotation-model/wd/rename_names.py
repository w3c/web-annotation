
fh = file('index-nametemplate.html')
data = fh.read()
fh.close()

names = ["Alice", "Beatrice", "Corina", "Dawn", "Emily", "Franceska", 
	"Gretchen", "Hannah", "Irina", "Jane", "Kelly", "Megan", "Noelle", "Ophelia",
	"Petra", "Qitara", "Ramona", "Sally", "Teynika", "Ulrika", "Valeria", "Wendy", 
	"Xena", "Yadira", "Zara", "Alexandra", "Britney", "Carla", "Devina", "Erin",
	"Felicity"]

while data.find('%%name%%') > -1:
	data = data.replace("%%name%%", names.pop(0), 1)

x = 0
while data.find("%%anno%%") > -1:
	x += 1
	data = data.replace("%%anno%%", str(x), 2)

fh = file('index-respec.html', 'w')
fh.write(data)
fh.close()

print "Now run respec in the page to generate static index.html"
