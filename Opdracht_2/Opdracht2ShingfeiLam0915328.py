def RGBtoHSL(R,G,B):
	cmin = min(R,G,B)
	cmax = max(R,G,B)
	hueInput = 60
	
	deltaCmaxCmin = cmax - cmin
	sumCmaxCmin = cmax + cmin
	
	# Used formula from the presentation and provided document.
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


def hueToRGB(p, q, t): #convert hue to RGB
    if(t<0):
        t+=1
    if(t>1):
        t-=1
    if(t < (1/6)):
        return p + (q-p) * 6 * t
    if(t < 1/2): 
        return q
    if(t < 2/3):
        return p + (q - p) * (2/3 - t) * 6
    return p

def HSLtoRGB(H,S,L):
	H = H/360
	S = S/100
	L = L/100

	if(S == 0):
		return(L,L,L)
	else:
		if(L < 0.5):
			q = L * (1 + S)
		else:
			q = L + S - L * S

	p = 2 * L - q

	R = hueToRGB(p, q, H + 1/3)*255
	G = hueToRGB(p, q, H)*255
	B = hueToRGB(p, q, H - 1/3)*255

	print('HSLtoRGB conversion')
	print('Red :', R)
	print('Green :', G)
	print('Blue:', B,'\n')

'''
HSLtoRGB & RGBtoHSL
'''
#Insert a number between 0-1 (R,G,B)
RGBtoHSL(1,1,0)

HSLtoRGB(120,10,10)

def RGBtoCMY(R,G,B):
	# Original function -> C = (1-R-K)/(1-K), but K isn't used or relevant.
	# Function C = 1-R is used.
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

	# Original function -> R = 255 * (1-C) * (1-K).
	# didn't use 255 en K so R= 1-C is used.

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
	# Formula used from the presentation (R,G,B) res = alpha(R,G,B)b before + (1-alpha)(R,G,B) after
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

