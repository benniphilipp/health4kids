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



});