
def RGBtoHSL(R,G,B):
	cmin = min(R,G,B)
	cmax = max(R,G,B)
	hueCalc = 60
	deltaC = cmax - cmin
	sumC = cmax + cmin
	
	if deltaC == 0:
		H = 0
	elif R == cmax:
		H = hueCalc *(((G-B)/deltaC)%6)
	elif G == cmax:
		H = hueCalc * (((B-R)/deltaC) + 2)
	else:
		H = hueCalc * (((R-G)/deltaC) + 4)
	
	S = (deltaC/(1 - (abs(sumC)-1)))*100
	L = (sumC/2)*100
	
	print('RGBtoHSL convertion')
	print('Hue (H) :', H,' o')
	print('Saturation (S) :', S,' %')
	print('Lightness (L) :', L,' %')

def HSLtoRGB(H,S,L):
	
	cmin = L + S* abs(L - (1/2)) - ((1/2)*S)
	cmin = L - S* abs(L - (1/2)) + ((1/2)*S)
	
	if H < 60:
		R = C
		G = X
		B = 0
	elif H < 120:
		R = X
		G = C
		B = 0
	elif H < 180:
		R = 0
		G = C
		B = X
	elif H < 240:
		R = 0
		G = X
		B = C
	elif H< 300:
		R = X
		G = 0
		B = C
	else
		R = C
		G = 0
		B = X
	
#Insert a number between 0-1 (R,G,B)
RGBtoHSL(1,1,0)

