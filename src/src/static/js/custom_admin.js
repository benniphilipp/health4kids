/*Backend Page Select*/

document.addEventListener("DOMContentLoaded", function() {
    const linkChoice = document.querySelector("#id_link_choice");
    const pageLabelField = document.querySelector("#panel-child-hero-link_url-section");
    const linkLabelField = document.querySelector("#panel-child-hero-page_link-section");

    linkChoice.value = "page";
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

    // GalleryImageText
    const selectButton = document.querySelector('#content-0-value-link_type');
    const fieldButtonPage = document.querySelector('div[data-contentpath="button_page"]');
    const fieldButtonUrl = document.querySelector('div[data-contentpath="button_url"]');

    selectButton.value = "page";
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

    // Testimonial Silder
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
    

});