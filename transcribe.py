import time, os, re, subprocess
import numpy as np
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from send2trash import send2trash

model_name = 'base.en'
#tiny.en is fast but shit, use only for testing
#base.en is 1.5x slower, but better
#small.en is 2.5x slower than base.en, but the best
#medium.en cannot be handled by my shit 4GB RAM laptop

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
def predict(mname,size):
	size = round(size,-5)//100000
	if mname == 'tiny.en':
		return round(0.976*size+8.15,-1)
	elif mname == 'base.en':
		return round(1.444*size+28.,-18)
	elif mname == 'small.en':
		return round(4.583*size+43.309,-1)
	else:
		print(f'{c.red}Error: Invalid mname: {mname}{c.end}')
		return 0

#transcribe each file
for file in files:
	print(f'{c.blue}Transcribing: {c.pink}{file} {c.blue}File size: {c.pink}{os.path.getsize(file)//1000}KB {c.blue}... (~{c.pink}{predict(model_name,os.path.getsize(file))}s{c.blue}){c.end}')

	#Convert .wma to .mp3 (for otranscribe)
	# if file[-4:].lower() == '.wma':
	# 	print(f'{c.blue}Converting into .mp3 in background ...')
	# 	os.system(f'ffmpeg -i '+ file.replace(' ','\ ') + ' '+ file[:-4].replace(' ','\ ') +'.mp3 -hide_banner -loglevel panic')

	start = time.time()
	#transcribe
	result = model.transcribe(file,fp16=False,language='English',temperature=0.2)
	print(f'{c.blue}Done. Time took: {c.green}{round(time.time()-start)}s{c.end}')

	output = result['text'][1:]
	# output = output.replace('?','?\n')

	document = Document()

	document.add_paragraph(f'{file[:-4]}\n\nTranscriber - Michael Chen\nEmail:\nPhone:\n')
	p = document.add_paragraph(output)

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
		# send2trash(file)


