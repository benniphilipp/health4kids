/*Backend Page Select*/

document.addEventListener("DOMContentLoaded", function() {


    const linkChoice = document.querySelector("#id_link_choice");
    const linkLabelField = document.querySelector("#panel-child-startseiten_header-page_link-section");
    const pageLabelField = document.querySelector("#panel-child-startseiten_header-link_url-section");

    updateFieldVisibility();

    function updateFieldVisibility() {
        if (linkChoice.value === "page") {
            linkLabelField.style.display = "block";
            pageLabelField.style.display = "none";
        } else if (linkChoice.value === "extern") {
            linkLabelField.style.display = "none";
            pageLabelField.style.display = "block";
        } else {
            linkLabelField.style.display = "block";
            pageLabelField.style.display = "none";
        }
    }

    linkChoice.addEventListener("change", updateFieldVisibility);




    // Backend GalleryImageText
    const selectButton = document.querySelector('#content-0-value-link_type');
    const fieldButtonPage = document.querySelector('div[data-contentpath="button_page"]');
    const fieldButtonUrl = document.querySelector('div[data-contentpath="button_url"]');

    // selectButton.value = "page";
    updateFiledVisibilitySection();

    function updateFiledVisibilitySection(){
        if(selectButton.value == "page"){
            fieldButtonUrl.style.display = 'none';
            fieldButtonPage.style.display = 'block';
        }else if (selectButton.value == "extern"){
            fieldButtonPage.style.display = 'none';
            fieldButtonUrl.style.display = 'block';
        }else{
            fieldButtonUrl.style.display = 'none';
            fieldButtonPage.style.display = 'block'; 
        }
    };

    selectButton.addEventListener("change", updateFiledVisibilitySection);



    
    // Backend Testimonial Silder
    const selectTestimonial = document.querySelector("#content-2-value-slider_type");
    const imgPerson = document.querySelector('div[data-contentpath="img_person"]');
    const namePerson = document.querySelector('div[data-contentpath="name_person"]');
    const jobPerson = document.querySelector('div[data-contentpath="job_person"]');

    console.log(selectTestimonial.value);

    selectTestimonial.value === "slider";
    TestimonialSilder();
    function TestimonialSilder(){
        if(selectTestimonial.value === "slider"){
            imgPerson.style.display = "none";
            namePerson.style.display = "none";
            jobPerson.style.display = "none";
        }else if(selectTestimonial.value ==="testimonial"){
            imgPerson.style.display = "block";
            namePerson.style.display = "block";
            jobPerson.style.display = "block";
        }else{
            imgPerson.style.display = "none";
            namePerson.style.display = "none";
            jobPerson.style.display = "none";
        }
    }

    selectTestimonial.addEventListener("change", TestimonialSilder);



    

    // Feld Validator
    function addCharacterCount(elementSelector) {
        var element = document.querySelector(elementSelector);
    
        if (element) {
            var classNames = element.className.split(' ');
            var maxLengthClass = classNames.find(function(className) {
                return className.startsWith('max_length-');
            });
    
            if (maxLengthClass) {
                var maxChars = parseInt(maxLengthClass.split('-')[1]);
    
                // Extrahiere den Textinhalt aus dem Datenattribut data-text="true"
                var textContentElement = element.querySelector('[data-text="true"]');
    
                // Füge die Anzahl der Zeichen direkt in das HTML des Elements ein
                var charCountElement = document.createElement('span');
    
                // Setze die Schriftfarbe auf Grau (hex: #808080)
                charCountElement.style.color = '#808080';
    
                charCountElement.innerText = ' Eingegebene Zeichen: ' + textContentElement.innerText.length + ' von ' + maxChars;
                element.appendChild(charCountElement);
            }
        }
    }

    addCharacterCount('[data-contentpath="heading"] .max_length-66');
    addCharacterCount('[data-contentpath="paragraph"] .max_length-364');

    function addCharacterCountForParagraph(elementSelector) {
        var element = document.querySelector(elementSelector);
    
        if (element) {
            var classNames = element.className.split(' ');
            var maxLengthClass = classNames.find(function(className) {
                return className.startsWith('max_length-');
            });
    
            if (maxLengthClass) {
                var maxChars = parseInt(maxLengthClass.split('-')[1]);
            
                // Extrahiere den Textinhalt direkt aus dem inneren <div>
                var innerDivElement = element.querySelector('div'); // Hier musst du den richtigen Selektor verwenden
                var textContent = innerDivElement ? innerDivElement.textContent || innerDivElement.innerText : '';
            
                // Füge die Anzahl der Zeichen direkt in das HTML des Elements ein
                var charCountElement = document.createElement('span');
            
                // Setze die Schriftfarbe auf Grau (hex: #808080)
                charCountElement.style.color = '#808080';
            
                charCountElement.innerText = ' Eingegebene Zeichen: ' + textContent.length + ' von ' + maxChars;
                element.appendChild(charCountElement);
            }
        }
    }

    addCharacterCountForParagraph('[data-contentpath="subline"] .max_length-89');
    addCharacterCountForParagraph('[data-contentpath="button_text"] .max_length-90');


    

});