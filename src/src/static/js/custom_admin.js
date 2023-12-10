/*Backend Page Select*/

document.addEventListener("DOMContentLoaded", function() {

    // Contact steps
    const selectContactSteps = document.querySelector(".select-contact-steps");
    const selectContactStepsPage = document.querySelector(".select-contact-steps-page");
    const selectContactStepsUrl = document.querySelector(".select-contact-steps-url");

    selectContactStepsFunc();

    function selectContactStepsFunc(){
        const selectContactStepsValue = document.querySelector(".select-contact-steps select");
        
        if (!selectContactStepsValue) {
            return;
        }

        const selectContactStPage = findLabel(selectContactStepsPage);
        const selectContactStUrl = findLabel(selectContactStepsUrl);

        if(selectContactStepsValue.value === "page"){
            if (selectContactStPage) {
                selectContactStepsUrl.style.display = 'none';
                selectContactStUrl.style.display = 'none';
                selectContactStepsPage.style.display = 'block';
                selectContactStPage.style.display = 'block';
            }
        }else if(selectContactStepsValue.value === "extern"){
            if (selectContactStUrl) {
                selectContactStepsPage.style.display = 'none';
                selectContactStPage.style.display = 'none';
                selectContactStepsUrl.style.display = 'block';
                selectContactStUrl.style.display = 'block';
            }
        }

    }

    const selectContactStepsValue = document.querySelector(".select-contact-steps");
    if(selectContactStepsValue){
        selectContactSteps.addEventListener('click', selectContactStepsFunc);
    }



    // Video
    const selectVideo = document.querySelector(".select-video");
    const selectVideoPage = document.querySelector(".select-video-page");
    const selectVideoUrl = document.querySelector(".select-video-url");

    selectVideoFunc();
    function selectVideoFunc(){
        const selectVideoValue = document.querySelector(".select-video select");
        
        if (!selectVideoValue) {
            return;
        }

        const selectViPage = findLabel(selectVideoPage);
        const selectViUrl = findLabel(selectVideoUrl);

        if(selectVideoValue.value === "page"){
            if (selectViPage) {
                selectViUrl.style.display = 'none';
                selectVideoUrl.style.display = 'none';
                selectVideoPage.style.display = 'block';
                selectViPage.style.display = 'block';
            }
        }else if(selectVideoValue.value === "extern"){
            if (selectViUrl) {
                selectVideoPage.style.display = 'none';
                selectViPage.style.display = 'none';
                selectVideoUrl.style.display = 'block';
                selectViUrl.style.display = 'block';
            }
        }

    }

    const selectVideoValue = document.querySelector(".select-video");
    if(selectVideoValue){
        selectVideo.addEventListener('click', selectVideoFunc)
    }

    // Text Image Einfach
    const selectTextImageOne = document.querySelector(".select-text-image-one");
    const selectTextImageOnePage = document.querySelector(".select-text-image-one-page");
    const selectTextImageOneUrl = document.querySelector(".select-text-image-one-url");

    selectTextOneFun();

    function selectTextOneFun(){
        
        const selectTextImageOneValue = document.querySelector(".select-text-image-one select");

        if (!selectTextImageOneValue) {
            return;
        }

        const selectTextOnePage = findLabel(selectTextImageOnePage);
        const selectTextOneUrl = findLabel(selectTextImageOneUrl);

        if(selectTextImageOneValue.value == "page"){
            if (selectTextOnePage) {
                selectTextOneUrl.style.display = 'none';
                selectTextImageOneUrl.style.display = 'none';
                selectTextImageOnePage.style.display = 'block';
                selectTextOnePage.style.display = 'block';
            }
        } else if(selectTextImageOneValue.value == "extern"){
            if (selectTextOneUrl) {
                selectTextOnePage.style.display = 'none';
                selectTextImageOnePage.style.display = 'none';
                selectTextImageOneUrl.style.display = 'block';
                selectTextOneUrl.style.display = 'block';
            }
        }

    }

    const selectTextImageOneValue = document.querySelector(".select-text-image-one");
    if(selectTextImageOneValue){
        selectTextImageOne.addEventListener('change', selectTextOneFun);
    }


    // Promo Selctor
    const selectPromoBox = document.querySelector(".select-promo-box");
    const selectPromoBoxPage = document.querySelector(".select-promo-box-page");
    const selectPromoBoxUrl = document.querySelector(".select-promo-box-url");

    selectPromoFunc();

    function selectPromoFunc(){
        const selectPromoBoxValue = document.querySelector(".select-promo-box select");

        if (!selectPromoBoxValue) {
            return;
        }

        const selectPromoPage = findLabel(selectPromoBoxPage);
        const selectPromoUrl = findLabel(selectPromoBoxUrl);

        if(selectPromoBoxValue.value === "page"){
            if (selectPromoPage) {
                selectPromoBoxUrl.style.display = 'none';
                selectPromoUrl.style.display = 'none';
                selectPromoPage.style.display = 'block';
                selectPromoBoxPage.style.display = 'block';
            }
        }else if(selectPromoBoxValue.value === "extern"){
            if (selectPromoPage) {
                selectPromoPage.style.display = 'none';
                selectPromoBoxPage.style.display = 'none';
                selectPromoBoxUrl.style.display = 'block';
                selectPromoUrl.style.display = 'block';
            }
        }
    }

    const selectPromoBoxValue = document.querySelector(".select-promo-box select");
    if(selectPromoBoxValue){
        selectPromoBox.addEventListener('change', selectPromoFunc);
    }

    // Text Image Selector
    const selectTextImage = document.querySelector(".select-image-text");
    const selectTextImagePage = document.querySelector(".select-image-page");
    const selectTextImageUrl = document.querySelector(".select-image-url");

    selectTextImageFunc();

    function selectTextImageFunc(){

            const selectImageTextValue = document.querySelector(".select-image-text select");

            if (!selectImageTextValue) {
                return;
            }
            
            const selectTextPage = findLabel(selectTextImagePage);
            const selectTextUrl = findLabel(selectTextImageUrl);
            // console.log(selectImageTextValue.value)
    
            if(selectImageTextValue.value === "page"){
                // console.log('RUN page');
                if (selectTextPage) {
                    selectTextImageUrl.style.display = 'none';
                    selectTextUrl.style.display = 'none';
                    selectTextImagePage.style.display = 'block';
                    selectTextPage.style.display = 'block';
                }
            }else if(selectImageTextValue.value === "extern"){
                // console.log('RUN extern');
                if(selectTextUrl){
                    selectTextPage.style.display = 'none';
                    selectTextImagePage.style.display = 'none';
                    selectTextImageUrl.style.display = 'block';
                    selectTextUrl.style.display = 'block';
                }
        }
    }

    const selectImageTextValue = document.querySelector(".select-image-text select");

    if(selectImageTextValue){
        selectTextImage.addEventListener('change', selectTextImageFunc);
    }

    // Gallery Image Text Selector
    const selectGalleryImageText = document.querySelector(".select-gallery-image-text");
    const selectGalleryImageTextPage = document.querySelector(".select-gallery-image-text-page");
    const selectGalleryImageTextUrl = document.querySelector(".select-gallery-image-text-url");
        
    selectGalleryImageTextFunc();

    function selectGalleryImageTextFunc(){

        const selectGalleryImageTextValue = document.querySelector(".select-gallery-image-text select");

        if (!selectGalleryImageTextValue) {
            return;
        }

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

    const selectGalleryImageTextValue = document.querySelector(".select-gallery-image-text select");
    if(selectGalleryImageTextValue){
        selectGalleryImageText.addEventListener('change', selectGalleryImageTextFunc);
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
    