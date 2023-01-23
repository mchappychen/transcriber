import time, os, re, subprocess
import numpy as np
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from send2trash import send2trash #I use this to send .wma to trash

model_name = 'base.en'
#tiny.en is fast but bad, use only for testing
#base.en is 1.5x slower but better, so I use this
#small.en is super slow, maybe even slower while using otranscribe at the same time
#medium.en cannot be handled by my 4GB RAM laptop

#pink,red,yellow,green,blue,violet,end
class c:
   violet = '\033[95m'
   pink = '\033[94m'
   blue = '\033[96m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   end = '\033[0m'
   bold = '\033[1m'

#importing whisper takes 20s
print(f'{c.blue}Importing whisper ... (~20s){c.end}')
import whisper

print(f'{c.blue}loading model {model_name} ... (~2s){c.end}')
model = whisper.load_model(model_name)

#get all mp3 files
files = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:].lower() in ['.mp3','.m4a','.wma']]

#TODO -- add support for .WAV

#Prediction models for how long a model will take based on previous data
def predict(type,size,mname='base.en'):
	#size is in bytes, convert it to KB
	size = round(size,-3)//1000
	if type == 'mp3':
		return int(round(0.016*size+52.95))
	elif type == 'm4a':
		return int(round(0.012*size+66.83))
	elif type == 'wma':
		return int(round(0.02*size+46.51))
	else:
		print(f'{c.red}Error: Unknown type: {type}{c.end}')
		return 0

#transcribe each file
for file in files:
	print(f'{c.blue}Transcribing: {c.pink}{file} {c.blue}File size: {c.pink}{os.path.getsize(file)//1000}KB {c.blue}... (~{c.pink}{predict(file[-3:].lower(),os.path.getsize(file))}s{c.blue}){c.end}')

	#Convert .wma to .mp3 (for otranscribe)
	if file[-4:].lower() == '.wma':
		print(f'{c.blue}Converting into .mp3 in background ...')
		os.system(f'ffmpeg -i '+ file.replace(' ','\ ') + ' '+ file[:-4].replace(' ','\ ') +'.mp3 -hide_banner -loglevel panic')

	start = time.time()
	#transcribe
	result = model.transcribe(file,fp16=False,language='English',temperature=0.2)
	print(f'{c.blue}Done. Time took: {c.green}{round(time.time()-start)}s{c.end}')

	#Gets rid of the weird space in the beginning
	output = result['text'][1:]

	# TODO -- find ways to output better
	# output = output.replace('?','?\n')

	#Add content to word doc
	document = Document()
	document.add_paragraph(f'{file[:-4]}\n\nTranscriber - Michael Chen\nEmail: mchappychen@gmail.com\nPhone: 614-940-1914\n')
	p = document.add_paragraph(output)

	#style the document
	for paragraph in document.paragraphs:
		paragraph.style = document.styles['Normal']
		for run in paragraph.runs:
			run.font.size = Pt(16)
			run.font.name = 'Arial'

	document.save(f'{file[:-4]}.docx')
	# subprocess.call(['open',file[:-4]+'.docx'])

#trash all the .wma files
for file in files:
	if file[-4:].lower() == '.wma':
		print(f'{c.blue}Moving {c.pink}{file}{c.blue} to trash{c.end}')
		send2trash(file)


