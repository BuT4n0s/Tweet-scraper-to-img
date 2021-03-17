import imgkit
import random
num =3000
options = {'width': 600, 'height':500, 'disable-smart-width': ''}
for i in range (0,num):
	try:
		num -= 1
		out = "Dadsaysjokles_image/Dadsaysjokes"+ str(num)
		joke=open("Dadsaysjokes/Dadsaysjokes"+str(i)+".txt", "r").read()
		link = "http://localhost:8080/New folder/final.php?j="+joke+"&t="+str(random.randint(2,59))
		imgkit.from_url(link,out+".jpg",options)
	except :
		try:
			j= ""
			for c in joke:
			    if 0 <= ord(c) <= 127:
			    	j+=c
			    else:
			    	j+= " " 
			joke=j
			link = "http://localhost:8080/New folder/final.php?j="+joke+"&t="+str(random.randint(2,59))
			imgkit.from_url(link,out+".jpg",options)
		except:
			pass
	