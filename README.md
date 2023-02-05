## Transcribing tools

### Auto-transcriber does:
- Auto-transcribes .mp3, .m4a, .wma, .wav files, outputs it into .docx
- Formats the output into question-answer
- Converts .wma into .mp3 so you can use it on oTranscribe
- haven't tested this on windows

### oTranscribe helper does:
- Make transcribing pad bigger
- Makes file upload button bigger (so you can drag-drop to it easier)
- Cmd+E to capitalize an entire line (again, haven't tested on windows)

## How to use:
### If you want to use the auto-transcriber:
- Download transcribe.py into a folder
- Install its packages with pip (python-docx, send2trash, whisper, nltk)
- When you run it, it will find all audio files in that folder, transcribe it, and output in a .docx
- If you don't know how to run a python file, don't bother using this. I don't want you to make a mistake.

### If you just want to use the oTranscribe helper:
- Get the spellbee extension for autocorrection: [link](https://chrome.google.com/webstore/detail/spell-bee/dfbnahffpakjbdlccohcoglcnafhgnhm?hl=en-US)
- Once it's installed, download the .csv from this github
- Click on the spellbee extension options
- Personally, I would press Delete All since I don't like spellbee's default autocorrections, but it's optional
- Scroll down to Import Settings, select the .csv file you just downloaded
- The auto-correction should work on oTranscribe!
- Don't forget to disable this extension on websites in their options page

- Get the tampermonkey extension: [link](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)
- Go to [oTranscribe.user.js](https://github.com/mchappychen/transcriber/blob/main/otranscribe.user.js) and click the Raw button to install it into tampermonkey
- Type [Command]+[e] on oTranscribe to auto-capitalize an entire line!


Personal Transcribing Tips:
1. If you use Brave browser, you can disable the annoying download shelf at the bottom: ![ss](https://i.imgur.com/CWkjmWe.png)

2. If you made a spelling mistake, you can add it to Spellbee so that it'll be auto-corrected next time.

3. oTranscribe has hotkeys to pause/skip backwards. You can change the hotkeys as well

4. oTranscribe can't export as .docx or .rtf (yet) so just copy-paste it into Google Docs or Word to export it

Currently working on:
- Adding a tutorial for oTranscribe

Ideas I have but won't work on:
- Re-training a Whisper model to fit your own audios
- My own webpage that'll combine all the features in this project
- Export oTranscribe pad as .rtf or .docx
- Exporting .csv file of typos for Spellbee for all the mistakes made in oTransribe

