
"""
1.Programare bazată pe reguli (PBR)
1.Tehnici de programare pe platforma Android (TPPA)
1.Aspecte computaţionale în teoria numerelor (ACTN)
1.Game Design-GD(Proiectarea jocurilor)

2.Psihologia comunicarii profesionale in domeniul IT- lui (PCPIT)
2.Cloud Computing (CC)
2.Tehnici de ingineria limbajului natural (TILN)
2.Analiza reţelelor media sociale (ARMS)

3.Reţele Petri şi aplicaţii (RPA)
3.Smart Card-uri si Aplicatii (SCA)
3.Topici speciale de programare .NET (TSP.NET)
"""
"""
1.1. Considerand materiile pe care le-ati avut pana acum la facultate, ce va pasioneaza cel mai mult?
	a.Limbajele C-like(PBR)
	b.aplicatii pe Android(TPPA)
	c.Matematica(ACTN)
	d.jocuri in Unity(GD)
1.2. Ce v-a atras cel mai mult la o materie, pana acum?
	a. Daca se trecea usor(PBR)
	b. Sa se noteze fiecare laborator(TPPA)
	c. Sa mai fac glume cu profesorul pt o atmosfera buna(ACTN)
	d. Sa fie permis sa mai stai pe telefon (GD)
1.3. Cati ani aveti?
	a.18(PBR)
	b.19(TPPA)
	c.20(ACTN)
	d.21(GD)

2.1. Care este materia dvs. preferata de pana acum?
	a. ML(PCPIT)
	b. Python(CC)
	c. Structuri de date(TILN)
	d. Logica(ARMS)
2.2. Ce v-a placut cel mai mult la un profesor?
	a. Ca stia cum sa isi predea materia(PCPIT)
	b. Ca trecea usor elevii la materie(CC)
	c. Ca avea simtul umorului(TILN)
	d. Ca era dur(ARMS)
2.3. Ce procesor aveti?
	a.I3(PCPIT)
	b.I5(CC)
	c.I7(TILN)
	d.I9(ARMS)

3.1 Ce viteza aveti la internet?
	a.100mb(RCA)
	b.200mb(SPA)
	c.300mb(TSP.net)
	d.1gb(TSP.net)
3.2 Cati prieteni buni aveti?
	a.1(RCA)
	b.2(SPA)
	c.3(TSP.net)
	d.4(TSP.net)
3.3 Cate surori/frati aveti?
	a.0(RCA)
	b.1(SPA)
	d.2(TSP.net)
	e.3+(TSP.net)
"""

def mostCommonAnswer(l):#ca sa vedem care raspuns apare cel mai mult
	c=0
	num=l[0]
	for i in l:
		curr_freq=l.count(i)
		if(curr_freq>c):
			c=curr_freq
			num=i
	return num

def helpdesk():
	suggest1=[]
	print("Considerand materiile pe care le-ati avut pana acum la facultate, ce va pasioneaza cel mai mult?")
	print("-------1.Limbajele C-like")
	print("-------2.aplicatii pe Android")
	print("-------3.Matematica")
	print("-------4.jocuri in Unity")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest1+=val

	print("1.2. Ce v-a atras cel mai mult la o materie, pana acum?")
	print("-------a. Daca se trecea usor")
	print("-------b. Sa se noteze fiecare laborator")
	print("-------c. Sa mai fac glume cu profesorul pt o atmosfera buna")
	print("-------d. Sa fie permis sa mai stai pe telefon ")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest1+=val

	print("Cati ani aveti?")
	print("-------1. 18")
	print("-------2. 19")
	print("-------3. 20")
	print("-------4. 21")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest1+=val


	suggest2=[]

	print("Care este materia dvs. preferata de pana acum?")
	print("-------1.ML")
	print("-------2.Python")
	print("-------3.Structuri de date")
	print("-------4.Logica")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest2+=val

	print("Ce v-a placut cel mai mult la un profesor?")
	print("-------1.Ca stia cum sa isi predea materia")
	print("-------2.Ca trecea usor elevii la materie")
	print("-------3.Ca avea simtul umorului")
	print("-------4.Ca era dur")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest2+=val

	print("Ce procesor aveti?")
	print("-------1.I3")
	print("-------2.I5")
	print("-------3.I7")
	print("-------4.Altul")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 4):")
	suggest2+=val


	suggest3=[]
	print("Ce viteza aveti la internet?")
	print("-------1.100mb")
	print("-------2.200mb")
	print("-------3.300mb")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 3):")
	suggest3+=val

	print("Cati prieteni buni aveti?")
	print("-------1. 1")
	print("-------2. 2")
	print("-------3. 3+")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 3):")
	suggest3+=val

	print("Cate surori/frati aveti?")
	print("-------1. 0")
	print("-------2. 1")
	print("-------3. 2+")
	val=input("Introduceti raspunsul pentru intrebare(doar numar intre 1 si 3):")
	suggest3+=val

	mcs1=mostCommonAnswer(suggest1)#most common answer, set 1 
	mcs2=mostCommonAnswer(suggest2)
	mcs3=mostCommonAnswer(suggest3)
	print("-----------------------------Sugestii--------------------------------------")
	if(int(mcs1)==1):
		print("Materia care vi s-ar potrivi dvs. din primul pachet este Programare bazata pe reguli(PBR)")
	elif(int(mcs1)==2):
		print("Materia care vi s-ar potrivi dvs. din primul pachet este Tehnici de programare pe platforma Android (TPPA)")
	elif(int(mcs1)==3):
		print("Materia care vi s-ar potrivi dvs. din primul pachet este Aspecte computaţionale în teoria numerelor (ACTN)")
	elif(int(mcs1)==4):
		print("Materia care vi s-ar potrivi dvs. din primul pachet este Game Design-GD(Proiectarea jocurilor)")

	if(int(mcs2)==1):
		print("Materia care vi s-ar potrivi dvs. din al doilea pachet este Psihologia comunicarii profesionale in domeniul IT- lui (PCPIT))")
	elif(int(mcs2)==2):
		print("Materia care vi s-ar potrivi dvs. din al doilea pachet este Cloud Computing (CC)")
	elif(int(mcs2)==3):
		print("Materia care vi s-ar potrivi dvs. din al doilea pachet este Tehnici de ingineria limbajului natural (TILN)")
	elif(int(mcs2)==4):
		print("Materia care vi s-ar potrivi dvs. din al doilea pachet este Analiza reţelelor media sociale (ARMS)")

	if(int(mcs3)==1):
		print("Materia care vi s-ar potrivi dvs. din al treilea pachet este Reţele Petri şi aplicaţii (RPA)")
	elif(int(mcs3)==2):
		print("Materia care vi s-ar potrivi dvs. din al treilea pachet este Smart Card-uri si Aplicatii (SCA)")
	elif(int(mcs3)==3):
		print("Materia care vi s-ar potrivi dvs. din al treilea pachet este Topici speciale de programare .NET (TSP.NET)")
helpdesk()
print("-----------------")
print(int(str("-1")))