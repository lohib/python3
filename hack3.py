def is_leap(year):
	leap=False
	if year%4==0:
		if year%100==0 and  not year%400==0:
			leap=False
		else:
		    leap=True
	return leap	    	
		

year=2004
print(is_leap(year))		

year=1990
print(is_leap(year))

year=1996
print(is_leap(year))
