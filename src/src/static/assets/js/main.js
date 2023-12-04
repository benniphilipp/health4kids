import '../../../../../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js';
import Swiper from 'swiper/bundle';

document.addEventListener('DOMContentLoaded', function() {


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

});