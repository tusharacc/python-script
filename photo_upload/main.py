import os,shutil


#MY_PATH = ['/home/tushar/Pictures/Marraige Photos/DCIM/100EOS5D/']
MY_PATH = ['/home/tushar/Pictures/Marraige Photos/DCIM/100EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/101EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/EOSMISC/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 2/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 2/']

OUTPUT_PATH = '/home/tushar/Pictures/Marraige Photos/final_photos/'

FILE_PATH = '/home/tushar/PhotosList.txt'

applicable_photos = []
f = open(FILE_PATH,'r')
for line in f:
	if line.strip() != '':
		print (line.strip())
		applicable_photos.append(line.strip()) 
	#print (len(applicable_photos))

for path in MY_PATH:
	images = os.listdir(path)
	for image in images:
		#print (image.split('.')[0])
		try:
			if applicable_photos.index(image.split('.')[0]) >= 0:
				shutil.copyfile(path+image,OUTPUT_PATH+image) 
		except ValueError:
			pass
