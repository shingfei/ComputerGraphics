def RGBtoHSL(R,G,B):
	cmin = min(R,G,B)
	cmax = max(R,G,B)
	hueInput = 60
	
	deltaCmaxCmin = cmax - cmin
	sumCmaxCmin = cmax + cmin
	
	#Hieronder staan de formules die op de docementatie stond.
	if deltaCmaxCmin == 0 or deltaCmaxCmin < 0:
		H = 0
	elif R == cmax:
		H = hueInput *(((G-B)/deltaCmaxCmin)%6)
	elif G == cmax:
		H = hueInput * (((B-R)/deltaCmaxCmin) + 2)
	elif B == cmax:
		H = hueInput * (((R-G)/deltaCmaxCmin) + 4)
	else:
		print('Only positieve numbers for R, G or B')
	
	S = (deltaCmaxCmin/(1 - (abs(sumCmaxCmin)-1)))*100
	L = (sumCmaxCmin/2)*100
	
	print('RGBtoHSL conversion')
	print('Hue (H) :', H,' o')
	print('Saturation (S) :', S,' %')
	print('Lightness (L) :', L,' %\n')

def HSLtoRGB(H,S,L):
	cmin = L + S* abs(L - 0.5)- 0.5*S
	cmax = L - S* abs(L - 0.5) + 0.5*S
	modH = H % 360
	deltaCmaxCmin = cmax - cmin
	
	#Formules vanuit de docementatie geimplementeerd 
	def HtoB(H):
		if 0 <= (modH) <120:
			B = cmin
			return B
		elif 120 <= (modH) <180:
			B = cmin + (deltaCmaxCmin) * ((modH - 120)/60)
			return B
		elif 180 <= (modH) < 300:
			B = cmax
			return B
		elif 300 <=(modH) < 360:
			B = cmax - (deltaCmaxCmin) * ((modH - 300)/60)
			return B
		else:
			print('try again')
			
	B = HtoB(H)
	G = HtoB(H + 120)
	R = HtoB(H - 120)
	
	print('HSLtoRGB conversion')
	print('R:', R)
	print('G:', G)
	print('B:', B,'\n')
'''
HSLtoRGB & RGBtoHSL
'''
#Insert a number between 0-1 (R,G,B)
RGBtoHSL(1,1,0)

HSLtoRGB(120,0.5,0.5)

def RGBtoCMY(R,G,B):
	#De orignele functie was C = (1-R-K)/(1-K), maar K is het niet
	#relevant voor het berekenen naar CMY in deze methode en dus C = 1 - R
	if R < 0 or G <0 or B <0:
		print('only positive numbers') 
	else:
		C = 1 - R
		M = 1 - G
		Y = 1 - B
	print('RGBtoCMY conversion')
	print('C :', C)
	print('M :', M)
	print('Y :', Y,'\n')

def CMYtoRGB(C,M,Y):
	#Orginele functie -> R = 255 * (1-C) * (1-K). 255 wordt niet gebruikt en K ook niet
	#dus blijft R = 1-C over.
	if C < 0 or M < 0 or Y < 0:
		print('only positive numbers') 
	else:
		R = 1 - C
		G = 1 - M
		B = 1 - Y
	print('CMYtoRGB conversion')
	print('R :', R)
	print('G :', G)
	print('B :', B,'\n')

'''
RGBtoCMY & CMYtoRGB
'''

RGBtoCMY(0.25,1,0.75)
CMYtoRGB(0.75,0,0.25)

def transparency(R1,G1,B1,alpha1,R2,G2,B2):
	
	oneMinusAlpha = 1 - alpha1
	#Formule van de presentatie gebruikt -> (R,G,B)res = alpha(R,G,B)voor + (1-alpha)(R,G,B)achter
	if R1 < 0 or G1 < 0 or B1 < 0 or alpha1 <0 or R2 < 0 or G2 < 0 or B2<0:
		print('Only positieve numbers')
	else:
		R = alpha1*R1 + oneMinusAlpha * R2
		G = alpha1*G1 + oneMinusAlpha * G2
		B = alpha1*B1 + oneMinusAlpha * B2
	print('Transparency values:')
	print('R :', R)
	print('G :', G)
	print('B :', B,'\n')
	
#Values between 0 and 1 -> example transparency(0.1,1,1,0,0.8,1,0.5)
transparency(0.5,1,0,0.5,1,0,0)

