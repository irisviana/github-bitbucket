
def verify_encode_magazine_luiza(title_ver,price_ver,rating_ver):

		title=None
		price=None
		rating=None

		if(len(title_ver) !=0):
			
			title=title_ver[0].encode('utf-8')

		if(len(price_ver)!=0):
			
			price=float(price_ver[0].encode('utf-8').replace('.','').replace(',','.'))

		if(rating_ver is not None):
			
			rating=float(rating_ver.encode('utf-8').replace(',','.'))

		return title,price,rating

def get_magazine_rating_and_numval(r,n):

	    rating=None
	    num_val=None
	    
	    if(r is not None):

	        rating=r.split()[1]

	    if(n is not None):

	        num_val=[int(s) for s in n.split() if s.isdigit()][0]

	    return rating,num_val

def verify_encode_mercado_livre(title_ver,price_ver,rating_ver,val_ver):

		title=None
		price=None
		rating=None
		val=None

		if(len(title_ver) !=0):
			
			title=title_ver[0].encode('utf-8')

		if(len(price_ver)!=0):
			
			if(price_ver[2].encode('utf-8')==','):
				
				price=float(price_ver[1].encode('utf-8').replace('.','')+'.'+price_ver[3].encode('utf-8'))
			else:
				price=float(price_ver[1].encode('utf-8'))
			
		if(rating_ver is not None):
			
			rating=float(rating_ver.encode('utf-8').replace(',','.'))

		if(val_ver is not None):
			
			val=[int(s) for s in val_ver.encode('utf-8').split() if s.isdigit()][0]
			

		return title,price,rating,val