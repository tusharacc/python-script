import os
from PIL import Image

f = open('image-dimensions.txt','w')

MY_PATH = ['/home/tushar/Pictures/Marraige Photos/DCIM/100EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/101EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/EOSMISC/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 2/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 2/']
OUTPUT_PATH = '/home/tushar/Pictures/Marraige Photos/Converted/'
for path in MY_PATH:
	images = os.listdir(path)
	for image in images:
		if image.split('.')[-1] == 'JPG':
			im = Image.open(path +image)
			im.save(OUTPUT_PATH+image.split('.')[0],'PNG',compress_level
=0)
