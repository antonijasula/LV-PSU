ime_datoteke = input("Ime datoteke: ")
dat_dir = "C:\\Users\\Antonija\\Desktop\\LV1-PSU\\Zad4\\"+ime_datoteke

try:
    datoteka = open(dat_dir, 'r')
except:
    print("Datoteka ne postoji!")
suma = 0
brojac = 0

for line in datoteka:
    line = line.rsplit()
    if ("X-DSPAM-Confidence:" in line):
        brojac += 1
        suma += float(line[1])

print("Average X-DSPAM-Confidence: ", suma/brojac)

datoteka.close()