f1 = open("ids.txt", "r")
f2 = open("urls.txt", "w")
ids = f1.readlines()

for id in ids:
	url = "https://www.youtube.com/watch?v=" + id
	f2.write(url + "\n")

f1.close()
f2.close()
