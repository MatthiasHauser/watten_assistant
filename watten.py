import sys
import numpy as np
#karten werden in einem 2d array dagestellt in aufsteigender Reihenfolge. mit Schell = 0, Herz = 1, Eichel = 2 & Laab = 3
#Bsp: Schell 7 = [0,0]
#zusätzlich wird Weli intern als höchst nummerierte Schell gewählt, also [0,8].
karten = [[0,1,2,3,4,5,6,7,8] , [0,1,2,3,4,5,6,7] , [0,1,2,3,4,5,6,7] , [0,1,2,3,4,5,6,7]]
stiche = [[] for i in range (5)] #es gibt maximal 5 Stiche in einer Runde.
potentiell_angesagte = []
def farbstich(a,b,c,d,trumpf):
	trumpffarbe = trumpf[0]
	trumpfschlag = trumpf[1]
	if (a[0] == trumpffarbe):
		return 0
	elif (b[0] == trumpffarbe):
		return 0
	elif (c[0] == trumpffarbe):
		return 0
	elif (d[0] == trumpffarbe):
		return 0
    #wenn Trumpffarbe nicht getroffen wurde, wird Trumpfschlag überprüft
	elif (a[1] == trumpfschlag):
		return 0
	elif (b[1] == trumpfschlag):
		return 0
	elif (c[1] == trumpfschlag):
		return 0
	elif (d[1] == trumpfschlag):
		return 0
	else:
		return 1
def stich(karte_a,karte_b,karte_c,karte_d,trumpf):
	trumpffarbe = trumpf[0]
	trumpfschlag = trumpf[1]
	guter = [trumpffarbe] #Der Gute ist die beste Karte im Spiel.
	if(trumpfschlag == 7):
		guter.append(0)
	elif(trumpfschlag == 8):
		guter.append(8) #wenn Weli angesagt ist, ist er selbst der Gute.
	else:
		guter.append(trumpfschlag+1)
    #nun von oben nach unten checken ob eine der Karten getroffen wurde.
    #als erstes: wurde der gute oder rechte getroffen:
    
    
    #guter:
	if(np.array_equal(karte_a, guter)):
		return karte_a
	elif(np.array_equal(karte_b, guter)):
		return karte_b
	elif(np.array_equal(karte_c, guter)):
		return karte_c
	elif(np.array_equal(karte_d, guter)):
		return karte_d
		
		
	#rechter:
	elif(np.array_equal(karte_a, trumpf)):
		return karte_a
	elif(np.array_equal(karte_b, trumpf)):
		return karte_b
	elif(np.array_equal(karte_c, trumpf)):
		return karte_c
	elif(np.array_equal(karte_d, trumpf)):
		return karte_d
	
	
	#linker,: weil alle Linken gleich gut sind, muss die Reihenfolge der Karten richtig eingegeben werden. eg Karte_a = erste gespielte Karte
	elif(karte_a[1] == trumpfschlag):
		return karte_a
	elif(karte_b[1] == trumpfschlag):
		return karte_b
	elif(karte_c[1] == trumpfschlag):
		return karte_c
	elif(karte_d[1] == trumpfschlag):
		return karte_d
	
	
	#nun geht es um Trumpffarbstiche:
	farben = [] #hier wird von allen KArten die die Trumpffarbe getroffen haben, die Zahl gespeichert.
	if(karte_a[0]==trumpffarbe):
		farben.append(karte_a[1])
	if(karte_b[0]==trumpffarbe):
		farben.append(karte_b[1])
	if(karte_c[0]==trumpffarbe):
		farben.append(karte_c[1])
	if(karte_d[0]==trumpffarbe):
		farben.append(karte_d[1])
	#jez wird die höchste Zahl aus den Trumpffarben rausgesucht
	hohe_karte = 0
	#Guter, Rechter und Linke müssen nicht explizit aussortiert werden, da sie sonst oben gestochen hätten.
	if((len(farben)) > 0):
		for i in range(0, len(farben)):
			if(farben[i] > hohe_karte):
				hohe_karte = farben[i]
	#jetzt wird geschaut welche der vier Karten die höchste Zahl(und gleichzeitig nicht Schlag, Guter, Rechter) hatte.
		if(karte_a[1]==hohe_karte):
			return karte_a
		if(karte_b[1]==hohe_karte):
			return karte_b
		if(karte_c[1]==hohe_karte):
			return karte_c
		if(karte_d[1]==hohe_karte):
			return karte_d
	
	
	#wurde kein einziger Trumpf getroffen geht es nun um Farbstiche:
	kein_trumpf = [karte_a[1]]
	hoher_farbstich = 0
	keine_weitere_farbe = 1 #bool
	if(karte_b[0]==karte_a[0]):
		kein_trumpf.append(karte_b[1])
		keine_weitere_farbe = 0
	if(karte_c[0]==karte_a[0]):
		kein_trumpf.append(karte_c[1])
		keine_weitere_farbe = 0
	if(karte_d[0]==karte_a[0]):
		kein_trumpf.append(karte_d[1])
		keine_weitere_farbe = 0
	if(keine_weitere_farbe):
		return karte_a
	else:
		for i in range(0, len(kein_trumpf)):
			if(kein_trumpf[i] > hoher_farbstich):
				hoher_farbstich = kein_trumpf[i]
		if(karte_a[1]==hoher_farbstich):
			return karte_a
		if(karte_b[1]==hoher_farbstich):
			return karte_b
		if(karte_c[1]==hoher_farbstich):
			return karte_c
		if(karte_d[1]==hoher_farbstich):
			return karte_d
temp = 0
def raten(a,b,c,d,stechende_karte):
	if(len(potentiell_angesagte)==0):
		for farbe in range(0,4):
			for schlag in range(0,8):
				versuche = [farbe,schlag]
				if(np.array_equal(stich(a,b,c,d,versuche),stechende_karte)): #es werden einfach alle karten getestet, wenn die stechende Karte mit der tatsächlich stechenden übereinstimmt, wird sie zum Array der potentiellen Angesagten hinzugefügt.
					potentiell_angesagte.append(versuche)
		if(np.array_equal(stich(a,b,c,d,(0,8)),stechende_karte)):
			potentiell_angesagte.append((0,8)) #weli wird nochmal extra überprüft weil er nicht in die Schleife passt.
	else:
		potentiell_angesagte[:] = [x for x in potentiell_angesagte if np.array_equal(stich(a,b,c,d,x),stechende_karte)] #list comprehension for the win
		#for pot in range(0, len(potentiell_angesagte)):
		#	potentiell_angesagte[:] = [x for x in potentiell_angesagte if np.array_equal(stich(a,b,c,d,potentiell_angesagte[pot]),stechende_karte)] #list comprehension for the win
			#print(potentiell_angesagte)
		#for pot in range(0, len(potentiell_angesagte)-temp): #bei weiteren Stichen nimmt er alle aus von vorigen Stichen geschlossenen potentiellen Angesagten und überprüft ob jene noch immer gültig sind.
		#	if(np.array_equal(stich(a,b,c,d,potentiell_angesagte[pot]),stechende_karte)==0):
		#		potentiell_angesagte.pop(pot)

def switch_farbe(x):
	return {
		0: "Schell",
		1: "Herz",
		2: "Eichel",
		3: "Laab"	
	}[x]

def switch_schlag(x):
	return {
		0: "Sieben",
		1: "Acht",
		2: "Neun",
		3: "Zehn",
		4: "Unter",
		5: "Ober",
		6: "Koenig",
		7: "Ass",
		8: "Weli"	
	} [x]
def ergebnis_ausgeben():
	if not potentiell_angesagte:
		print("Alle Karten sind möglich.")
	else:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("Folgende Karten könnten angesagt sein: \n")
		count = 1
		for pot in range (len(potentiell_angesagte)):
			y = 0
			x = potentiell_angesagte[pot][y]
			z = potentiell_angesagte[pot][y+1]
			print("Möglichkeit "+ str(count)+":"+switch_farbe(x)+" "+switch_schlag(z))
			print("\tin diesem Fall sind folgende Trümpfe noch im Spiel: ")
			rest_trumpf((x,z))
			count += 1
			#print("\n")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def eingabe(string):
	if string == "Schell":
		return 0
	elif string == "Herz":
		return 1
	elif string == "Eichel":
		return 2
	elif string == "Laab":
		return 3
	elif string == "Sieben":
		return 0
	elif string == "Acht":
		return 1
	elif string == "Neun":
		return 2
	elif string == "Zehn":
		return 3
	elif string == "Unter":
		return 4
	elif string == "Ober":
		return 5
	elif string == "König":
		return 6
	elif string == "Ass":
		return 7
	elif string == "Weli":
		return 8
	else:
		print("Falsche Eingabe:( Ripperoni")	
def add_stich():
	tp = [[0,0] for i in range(5)]
	print("Schell, Herz, Eichel, Laab")
	print("Sieben, Acht, Neun, ..., Ass")
	print("Erste ausgespielte Karte:")
	tp[0][0] = eingabe(input("Farbe:\t"))
	tp[0][1] = eingabe(input("Schlag:\t"))
	print("Zweite ausgespielte Karte:")
	tp[1][0] = eingabe(input("Farbe:\t"))
	tp[1][1] = eingabe(input("Schlag:\t"))
	print("Dritte ausgespielte Karte:")
	tp[2][0] = eingabe(input("Farbe:\t"))
	tp[2][1] = eingabe(input("Schlag:\t"))
	print("Vierte ausgespielte Karte:")
	tp[3][0] = eingabe(input("Farbe:\t"))
	tp[3][1] = eingabe(input("Schlag:\t"))
	num = int(input("Welche dieser Karten hat gestochen? (1-4)"))
	raten(tp[0],tp[1],tp[2],tp[3],tp[num-1])
	karten[tp[0][0]][tp[0][1]] = 10 #gespielte Karten werden auf 10 gesetzt.
	karten[tp[1][0]][tp[1][1]] = 10
	karten[tp[2][0]][tp[2][1]] = 10
	karten[tp[3][0]][tp[3][1]] = 10
	
def is_trumpf(karte, angesagte):
	if karte[0] == angesagte[0]:
		return 1
	elif karte[1] == angesagte[1]:
		return 1
	else:
		return 0
		
def rest_trumpf(angesagte):
	for farbe in range(4):
		for schlag in range(8):
			if karten[farbe][schlag] != 10:
				if is_trumpf((farbe,schlag), angesagte):
					print("\t\t"+switch_farbe(farbe)+" "+switch_schlag(schlag))

def main():
	
	while(1):
		print("[1] Stich hinzufügen, [2] Reset, [3] Programm beenden")
		x = int(input("Was möchten Sie tun? "))
		if(x==1):
			add_stich()
			ergebnis_ausgeben()
		elif(x==2):
			print("Reset durchgeführt\n")
			potentiell_angesagte = []
		elif(x==3):
			sys.exit()
		elif(x==4):
			ergebnis_ausgeben()
		else:
			print("Falscher Input, bitte gib 1, 2 oder 3 ein.")
  
main()
