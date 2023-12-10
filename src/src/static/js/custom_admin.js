/*Backend Page Select*/

document.addEventListener("DOMContentLoaded", function() {


    const selectGalleryImageText = document.querySelector(".select-gallery-image-text");
    const selectGalleryImageTextPage = document.querySelector(".select-gallery-image-text-page");
    const selectGalleryImageTextUrl = document.querySelector(".select-gallery-image-text-url");
        
    selectGalleryImageTextFunc();

    function selectGalleryImageTextFunc(){

        const selectGalleryImageTextValue = document.querySelector(".select-gallery-image-text select");
        const selectGalleryImagePage = findLabel(selectGalleryImageTextPage);
        const selectGalleryImageUrl = findLabel(selectGalleryImageTextUrl);

        if(selectGalleryImageTextValue.value === "page"){
            if (selectGalleryImagePage) {
                selectGalleryImageTextUrl.style.display = 'none';
                selectGalleryImageUrl.style.display = 'none';
                selectGalleryImageTextPage.style.display = 'block';
                selectGalleryImagePage.style.display = 'block';
            }
        }else if(selectGalleryImageTextValue.value === "extern"){
            if(selectGalleryImagePage){
                selectGalleryImageTextPage.style.display = 'none';
                selectGalleryImagePage.style.display = 'none';
                selectGalleryImageTextUrl.style.display = 'block';
                selectGalleryImageUrl.style.display = 'block';
            }
        }

    }

    function findLabel(element) {
        while (element) {
            var labelElement = element.querySelector('.w-field__label');
            if (labelElement) {
                return labelElement;
            }
            element = element.parentElement;
        }
    
        return null;
    }

    selectGalleryImageText.addEventListener('change', selectGalleryImageTextFunc);



    // function updateFieldVisibility() {
    //     if (linkChoice.value === "page") {
    //         linkLabelField.style.display = "block";
    //         pageLabelField.style.display = "none";
    //     } else if (linkChoice.value === "extern") {
    //         linkLabelField.style.display = "none";
    //         pageLabelField.style.display = "block";
    //     } else {
    //         linkLabelField.style.display = "block";
    //         pageLabelField.style.display = "none";
    //     }
    // }

    // linkChoice.addEventListener("change", updateFieldVisibility);




    // const linkChoice = document.querySelector("#id_link_choice");
    // const linkLabelField = document.querySelector("#panel-child-startseiten_header-page_link-section");
    // const pageLabelField = document.querySelector("#panel-child-startseiten_header-link_url-section");

    // updateFieldVisibility();

    // function updateFieldVisibility() {
    //     if (linkChoice.value === "page") {
    //         linkLabelField.style.display = "block";
    //         pageLabelField.style.display = "none";
    //     } else if (linkChoice.value === "extern") {
    //         linkLabelField.style.display = "none";
    //         pageLabelField.style.display = "block";
    //     } else {
    //         linkLabelField.style.display = "block";
    //         pageLabelField.style.display = "none";
    //     }
    // }

    // linkChoice.addEventListener("change", updateFieldVisibility);




    // // Backend GalleryImageText
    // const selectButton = document.querySelector('#content-0-value-link_type');
    // const fieldButtonPage = document.querySelector('div[data-contentpath="button_page"]');
    // const fieldButtonUrl = document.querySelector('div[data-contentpath="button_url"]');

    // // selectButton.value = "page";
    // updateFiledVisibilitySection();

    // function updateFiledVisibilitySection(){
    //     if(selectButton.value == "page"){
    //         fieldButtonUrl.style.display = 'none';
    //         fieldButtonPage.style.display = 'block';
    //     }else if (selectButton.value == "extern"){
    //         fieldButtonPage.style.display = 'none';
    //         fieldButtonUrl.style.display = 'block';
    //     }else{
    //         fieldButtonUrl.style.display = 'none';
    //         fieldButtonPage.style.display = 'block'; 
    //     }
    // };

    // selectButton.addEventListener("change", updateFiledVisibilitySection);




    
    // // Feld Validator
    // function addCharacterCount(elementSelector) {
    //     var element = document.querySelector(elementSelector);
    
    //     if (element) {
    //         var classNames = element.className.split(' ');
    //         var maxLengthClass = classNames.find(function(className) {
    //             return className.startsWith('max_length-');
    //         });
    
    //         if (maxLengthClass) {
    //             var maxChars = parseInt(maxLengthClass.split('-')[1]);
    
    //             // Extrahiere den Textinhalt aus dem Datenattribut data-text="true"
    //             var textContentElement = element.querySelector('[data-text="true"]');
    
    //             // Füge die Anzahl der Zeichen direkt in das HTML des Elements ein
    //             var charCountElement = document.createElement('span');
    
    //             // Setze die Schriftfarbe auf Grau (hex: #808080)
    //             charCountElement.style.color = '#808080';
    
    //             charCountElement.innerText = ' Eingegebene Zeichen: ' + textContentElement.innerText.length + ' von ' + maxChars;
    //             element.appendChild(charCountElement);
    //         }
    //     }
    // }

    // addCharacterCount('[data-contentpath="heading"] .max_length-66');
    // addCharacterCount('[data-contentpath="paragraph"] .max_length-364');

    // function addCharacterCountForParagraph(elementSelector) {
    //     var element = document.querySelector(elementSelector);
    
    //     if (element) {
    //         var classNames = element.className.split(' ');
    //         var maxLengthClass = classNames.find(function(className) {
    //             return className.startsWith('max_length-');
    //         });
    
    //         if (maxLengthClass) {
    //             var maxChars = parseInt(maxLengthClass.split('-')[1]);
            
    //             // Extrahiere den Textinhalt direkt aus dem inneren <div>
    //             var innerDivElement = element.querySelector('div'); // Hier musst du den richtigen Selektor verwenden
    //             var textContent = innerDivElement ? innerDivElement.textContent || innerDivElement.innerText : '';
            
    //             // Füge die Anzahl der Zeichen direkt in das HTML des Elements ein
    //             var charCountElement = document.createElement('span');
            
    //             // Setze die Schriftfarbe auf Grau (hex: #808080)
    //             charCountElement.style.color = '#808080';
            
    //             charCountElement.innerText = ' Eingegebene Zeichen: ' + textContent.length + ' von ' + maxChars;
    //             element.appendChild(charCountElement);
    //         }
    //     }
    // }

    // addCharacterCountForParagraph('[data-contentpath="subline"] .max_length-89');
    // addCharacterCountForParagraph('[data-contentpath="button_text"] .max_length-90');






});

/**
 * Initializes character and word counters for all richtext fields on the page.
 */
    function initializeCharacterCounters() {
        // Locate all main editor containers
        const editorWrappers = document.querySelectorAll('.w-field--draftail_rich_text_area');
      
        // If no editor containers exist, exit the function.
        if (!editorWrappers.length) {
          return;
        }
      
        // Iterate over each editor container
        editorWrappers.forEach((editorWrapper, index) => {

            const countersContainer = document.createElement('div');
            countersContainer.className = 'counters-container';

            // Create an element for the character counter
            const charCounter = document.createElement('div');
            charCounter.className = `char-counter-${index}`;
        
            // Create an element for the word counter
            const wordCounter = document.createElement('div');
            wordCounter.className = `word-counter-${index}`;

            countersContainer.appendChild(charCounter);
            countersContainer.appendChild(wordCounter);

        
            // Append the counters directly below the editor container
            editorWrapper.parentNode.insertBefore(countersContainer, editorWrapper.nextSibling);
        
            // Locate the contenteditable element
            const textField = editorWrapper.querySelector('.DraftEditor-editorContainer [contenteditable="true"]');
        
            // Function to update the character and word count
            const updateCounter = () => {
                const textContent = textField.textContent || "";
                const wordCount = textContent.split(/\s+/).filter(Boolean).length;
                charCounter.innerText = `Zeichen: ${textContent.length}`;
                wordCounter.innerText = `Wörter: ${wordCount}`;
            };
      
            // Attach event listeners
            textField.addEventListener('input', updateCounter);
            textField.addEventListener('keydown', (event) => {
                if (event.keyCode === 8 || event.keyCode === 46) {
                setTimeout(updateCounter, 50);
                }
            });
            textField.addEventListener('paste', () => setTimeout(updateCounter, 50));
        
            countersContainer.style.display = 'flex';
            countersContainer.style.gap = '10px'; // Set the desired gap
            // Set initial values
            updateCounter();
        });
      }
      
      /**
       * Initializes the mutation observer to monitor for added richtext fields.
       */
      function initObserver() {
        const observer = new MutationObserver((mutations) => {
          mutations.forEach((mutation) => {
            if (mutation.addedNodes && mutation.addedNodes.length > 0) {
              for (const node of mutation.addedNodes) {
                if (node.querySelector && node.querySelector('.w-field--draftail_rich_text_area')) {
                  initializeCharacterCounters();
                }
              }
            }
          });
        });
      
        observer.observe(document.body, {
          childList: true,
          subtree: true,
        });
      }
      
      // Initialize on page load and DOMContentLoaded
      window.addEventListener('load', initObserver);
      document.addEventListener('DOMContentLoaded', initializeCharacterCounters);
    