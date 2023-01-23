Stuff I use to help me transcribe

Auto-transcriber does:
- Auto-transcribes .mp3, .m4a, .wma files, outputs it into .docx
- Converts .wma into .mp3 so you can use it on oTranscribe
- idk if it works on windows

oTranscribe helper does:
- Make transcribing pad bigger
- Makes file upload button bigger (so you can drag-drop to it easier)
- Cmd+E to capitalize an entire line (idk if it works on windows)

How to use:
If you want to use the auto-transcriber:
- Download transcribe.py into a folder
- Install its packages with pip (python-docx, send2trash, whisper)
- When you run it, it will find all audio files in that folder, transcribe it, and output in a .docx
- If you don't know how to run a python file, don't bother using this. I don't want you to make a mistake.

If you just want to use the oTranscribe helper:
- Get the SpellBee and Tampermonkey extension
- Install oTranscribe.user.js into tampermonkey
- Import my list of spelling corrections for SpellBee 
- Disable spellbee extension on sites you don't want it on in their options

Tips:
1. If you use Brave browser, you can disable the annoying download shelf at the bottom: ![ss](https://i.imgur.com/CWkjmWe.png)

2. Have a drink next to you, make sure room-temp is hot enough for your fingers to move faster.

3. If you made a spelling mistake, you can add it to Spellbee so that it'll be auto-corrected next time.

4. oTranscribe has hotkeys to pause/skip backwards. You can change to hotkeys as well

Currently working on:
- Smart auto-correction algorithm by guessing what you were trying to type
- Formatting auto-transcriber's output better
- Adding a scribe tutorial for oTranscribe

Future ideas I probably won't work on:
- Re-training a Whisper model to fit your own audios
- My own webpage that'll combine all the features in this project
- Exporting .csv file of typos for Spellbee for all the mistakes made in oTransribe

