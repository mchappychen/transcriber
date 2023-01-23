// ==UserScript==
// @name         Capitalize Selection
// @version      1.1
// @description  Adds hotkey Cmd+e to capitalize a line in otranscribe
// @author       Michael
// @match        https://otranscribe.com/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=otranscribe.com
// @require      https://code.jquery.com/jquery-3.6.0.min.js
// ==/UserScript==
/* globals jQuery, $, waitForKeyElements */

(function() {

    //Wait a bit for page to load before modifying its content
    setTimeout(function(){
        //Enlarge editing pad
        $('#textbox').css('width','900px');
        //Move right-panel to the right
        $('.text-panel').css('left','calc(50% + 550px)');
        //Make the upload-audio section smaller
        $('.input.active').css('margin','5px auto');
        $('.alt-input-button').css('display','none');
        //Make button bigger for easier drag-drop
        $('.file-input-wrapper').css('width','90%');
        $('.file-input-wrapper').css('margin','1px auto 1px');
        $('#textbox').css('margin','10px auto');
        $('.btn-file-input').css('height','200px');
        //Hide the stupid text below the file input button
        $('#formats').css('display','none');
        $('#lastfile').css('display','none');
    },500);


    document.addEventListener('keydown', (event) => {
        // Detect if shift+e is pressed
        if (event.key == 'e' && event.metaKey) {

            var sel = window.getSelection();

            if(sel.anchorNode.nodeValue == sel.anchorNode.nodeValue.toUpperCase()){
                let lowerCase = sel.anchorNode.nodeValue.toLowerCase().replaceAll(' i ',' I ').replaceAll(" i've "," I've ").replaceAll(/(^|[.!?]\s+)([a-z])/g, function (m, $1, $2) {
                        return $1 + $2.toUpperCase();
                    });
                sel.anchorNode.nodeValue = lowerCase;
            } else {
                let upperCase = sel.anchorNode.nodeValue.toUpperCase();
                sel.anchorNode.nodeValue = upperCase;
            }

            /* Code below requires selecting something. Code above just requires clicking on the line
            //make sure there's actually something selected
            if (sel.rangeCount){
                //If it's all upper-case, turn it back to lower-case*
                //*unfortunately it removes line breaks
                if (sel.toString() == sel.toString().toUpperCase()){
                    let lowerCase = sel.toString().toLowerCase().replaceAll(' i ',' I ').replaceAll(/([.!?]\s+)([a-z])/g, function (m, $1, $2) {
                        return $1 + $2.toUpperCase();
                    });
                    let range = sel.getRangeAt(0);
                    range.deleteContents();
                    range.insertNode(document.createTextNode(lowerCase));
                } else {
                    let upperCase = sel.toString().toUpperCase();
                    sel.anchorNode.nodeValue = upperCase
                    let range = sel.getRangeAt(0);
                    range.deleteContents();
                    range.insertNode(document.createTextNode(upperCase));
                }
            }
            */
        }
    })
})();
