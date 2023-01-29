## Auto-transcribing tools

### Auto-transcriber does:
- Auto-transcribes .mp3, .m4a, .wma, .wav files, outputs it into .docx
- Formats the output the way I like
- Converts .wma into .mp3 so you can use it on oTranscribe
- haven't tested this on windows

### oTranscribe helper does:
- Make transcribing pad bigger
- Makes file upload button bigger (so you can drag-drop to it easier)
- Cmd+E to capitalize an entire line (again, haven't tested on windows)

## How to use:
If you want to use the auto-transcriber:
- Download transcribe.py into a folder
- Install its packages with pip (python-docx, send2trash, whisper, nltk)
- When you run it, it will find all audio files in that folder, transcribe it, and output in a .docx
- If you don't know how to run a python file, don't bother using this. I don't want you to make a mistake.

## If you just want to use the oTranscribe helper:
- Get the SpellBee and Tampermonkey extension
- Install oTranscribe.user.js into tampermonkey (click the [raw] button in https://github.com/mchappychen/transcriber/blob/main/otranscribe.user.js)
- Import my list of spelling corrections for SpellBee 
- Disable spellbee extension on sites you don't want it on in their options

Personal Transcribing Tips:
1. If you use Brave browser, you can disable the annoying download shelf at the bottom: ![ss](https://i.imgur.com/CWkjmWe.png)

2. If you made a spelling mistake, you can add it to Spellbee so that it'll be auto-corrected next time.

3. oTranscribe has hotkeys to pause/skip backwards. You can change the hotkeys as well

Currently working on:
- Adding a scribe tutorial for oTranscribe
- Optimizing "temperature" parameter for whisper's model

Ideas I have but won't work on:
- Re-training a Whisper model to fit your own audios
- My own webpage that'll combine all the features in this project
- Export oTranscribe pad as .rtf or .docx
- Exporting .csv file of typos for Spellbee for all the mistakes made in oTransribe

