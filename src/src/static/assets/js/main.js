import '../../../../../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js';
import Swiper from 'swiper/bundle';

document.addEventListener('DOMContentLoaded', function() {

    var gridImage = document.getElementById('image-grid');
    
    if(gridImage){
        var items = gridImage.getElementsByClassName('grid-item');
        items[1].classList.add('grid-item--width2');

        for (var i = 4; i < items.length; i += 2) {
            items[i].classList.add('grid-item--width2');
        }
    }


    const mySwiper = new Swiper('.mySwiper', {
        // Swiper-Konfiguration hier
        slidesPerView: 1,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });


    const OpenMenu = document.querySelector('#menuOpen');
    if(OpenMenu){
        OpenMenu.addEventListener('click', () => {
            const burgerMenu = document.querySelector('.burger-menu');
            burgerMenu.classList.toggle('active');

            const mobileMenuDiv = document.querySelector('#mobileMenuItem');
            mobileMenuDiv.classList.toggle('visible');

            const body = document.querySelector('body');
            body.classList.toggle('body-fixed');

        })
    }

    // Get Up button
    var mybutton = document.getElementById("scrollToTopBtn");

    window.onscroll = function () {
        scrollFunction();
    };

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            mybutton.style.display = "flex";
        } else {
            mybutton.style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    mybutton.addEventListener("click", function () {
        scrollToTop();
    });

    function scrollToTop() {
        if (document.body.scrollTop !== 0 || document.documentElement.scrollTop !== 0) {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    }


    // Function to open the popup
    function openPopup(src) {
        var popup = document.getElementById('imagePopup');
        var popupImage = document.getElementById('popupImage');
        
        if (popup && popupImage) {
            popupImage.src = src;
            popup.style.display = 'flex';
            document.body.style.overflow = 'hidden'; // Disable scrolling
        }
    }

    function closePopup() {
        var popup = document.getElementById('imagePopup');
        if (popup) {
            popup.style.display = 'none';
            document.body.style.overflow = 'auto'; // Enable scrolling
        }
    }

    var galleryImages = document.querySelectorAll('.gallery img');

    galleryImages.forEach(function(image) {
        image.addEventListener('click', function() {
            openPopup(image.src);
        });
    });

    var closeButton = document.getElementById('closePopup');
    if (closeButton) {
        closeButton.addEventListener('click', closePopup);
    }


    // Cookie Banner
    document.querySelectorAll(".cookie-accept-button").forEach(function(button) {
        button.addEventListener("click", function () {
            setDatenschutzCookie(true, "datenschutz_akzeptiert");
            document.getElementById("cookie-banner").style.display = "none";
            document.getElementById("popup").style.display = "none";
        });
    });
    
    document.querySelectorAll(".cookie-decline-button").forEach(function(button) {
        button.addEventListener("click", function () {
            setDatenschutzCookie(false, "datenschutz_nicht_einverstanden");
            document.getElementById("cookie-banner").style.display = "none";
            document.getElementById("popup").style.display = "none";
        });
    });

    function setDatenschutzCookie(akzeptiert, cookieName) {
        var expirationDate;
        
        if(cookieName === 'datenschutz_akzeptiert'){
            expirationDate = new Date(new Date().getTime() + 365 * 24 * 60 * 60 * 1000); // 1 Jahr Gültigkeit
        }else{
            expirationDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000); // 1 Tag Gültigkeit
        }
        
        document.cookie = cookieName + "=" + akzeptiert + "; expires=" + expirationDate.toUTCString() + "; path=/";
    }
    
    function hatBenutzerDatenschutzAkzeptiert(cookieName) {
        var name = cookieName + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var cookieArray = decodedCookie.split(';');

        for (var i = 0; i < cookieArray.length; i++) {
            var cookie = cookieArray[i].trim();
            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        return null;
    }

    function CookieFunctionsPw(){
        var datenschutz_nicht_einverstanden = hatBenutzerDatenschutzAkzeptiert("datenschutz_nicht_einverstanden");
        var datenschutz_akzeptiert = hatBenutzerDatenschutzAkzeptiert('datenschutz_akzeptiert')
    
        if(datenschutz_nicht_einverstanden === false || datenschutz_nicht_einverstanden === "false"){
            document.getElementById("cookie-banner").style.display = "none";    
        }else if(datenschutz_akzeptiert == true || datenschutz_akzeptiert == 'true'){
            document.getElementById("cookie-banner").style.display = "none";    
        }else if(datenschutz_nicht_einverstanden === null){
    
        }else if(datenschutz_akzeptiert == null){
            
        }
    }


    document.getElementById("openPopupButton").addEventListener("click", function() {
        document.getElementById("popup").style.display = "block";
    });
    
    document.getElementById("closePopupButton").addEventListener("click", function() {
        document.getElementById("popup").style.display = "none";
    });
    

    document.getElementById('cookie-delete-button').addEventListener("click", () =>{
        function deleteCookie(cookieName) {
            document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        }
        deleteCookie("datenschutz_nicht_einverstanden");

        function loescheDatenschutzCookie() {
            document.cookie = "datenschutz_akzeptiert=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        }
        loescheDatenschutzCookie();
        document.getElementById("popup").style.display = "none";
        document.getElementById("cookie-banner").style.display = "block";
        CookieFunctionsPw();

    });

    CookieFunctionsPw();




    // Formular Honypot
    var form = document.querySelector('.custom-form');

    if(form){
        form.addEventListener('submit', function(event) {
            var hiddenInput = document.querySelector('input[name="_name_pw"]');
            if (hiddenInput.value.trim() !== '') {
                //alert('Das Formular kann nicht abgesendet werden, wenn etwas im versteckten Feld steht.');
                event.preventDefault();
            }
        });
    }




});