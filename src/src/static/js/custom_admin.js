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

    
});