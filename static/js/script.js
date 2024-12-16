//step 1: get DOM
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = carouselDom.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
let timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 3000;
let timeAutoNext = 7000;

nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;
let runNextAuto = setTimeout(() => {
    next.click();
}, timeAutoNext)
function showSlider(type){
    let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        next.click();
    }, timeAutoNext)
}

  
//   for our-clients-section --
var copy = document.querySelector(".logos-slide").cloneNode(true);
document.querySelector(".logos").appendChild(copy);

// swiper
// var swiper = new Swiper(".slide-content", {
//     slidesPerView: 3,
//     spaceBetween: 25,
//     loop: true,
//     centerSlide: 'true',
//     fade: 'true',
//     grabCursor: 'true',
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//       dynamicBullets: true,
//     },
//     navigation: {
//       nextEl: ".swiper-button-next",
//       prevEl: ".swiper-button-prev",
//     },

//     breakpoints:{
//         0: {
//             slidesPerView: 1,
//         },
//         520: {
//             slidesPerView: 2,
//         },
//         950: {
//             slidesPerView: 3,
//         },
//     },
//   });
var swiper = new Swiper('.swiper-container', {
    loop: true,
    autoplay: {
        delay: 5000,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});
  $(document).ready(function(){
    $(".owl-carousel").owlCarousel();
  });
    $('.owl-carousel').owlCarousel({
      loop:true,
      margin:10,
      nav:false,
      Animation:true ,
      autoplay: true, 
    autoplayTimeout: 3000,
    loop: true,
    autoplayHoverPause: true,
    // Transition and animation settings
    animateOut: 'fadeOut', // Animation when leaving the item
    animateIn: 'fadeIn', // Animation when entering the item
    smartSpeed: 500, // Smooth speed
    autoplayTimeout: 5000, 
    autoplayHoverPause: true, 
    responsive:{
          0:{
              items:1
          },
          600:{
              items:3
          },
          1000:{
              items:5
          }
      }
  })
  document.addEventListener("DOMContentLoaded", function() {
    const videoContainer = document.querySelector(".video-container");
    const videoCards = document.querySelectorAll(".video-card");
    const bullets = document.querySelectorAll(".bollet");
    const controlBtns = document.querySelectorAll(".icon");
    const videoCardWidth = videoCards[0].offsetWidth;
    const videosPerPage = 3; // Number of videos per page
    let currentIndex = 0;

    // Function to update active video card style
    function setActiveVideo(index) {
        videoContainer.style.transition = "transform 0.5s ease-in-out";
        videoContainer.style.transform = `translateX(-${index * videoCardWidth * videosPerPage}px)`;
        currentIndex = index;
        updatePagination();
    }

    // Function to handle pagination when clicking on the bullets
    bullets.forEach((bullet, index) => {
        bullet.addEventListener("click", function() {
            setActiveVideo(index);
        });
    });

    // Function to update pagination when changing slides
    function updatePagination() {
        bullets.forEach((bullet, index) => {
            if (index === currentIndex) {
                bullet.classList.add("active");
            } else {
                bullet.classList.remove("active");
            }
        });
    }

    // Function to show next set of video cards
    function showNextSet() {
        const nextIndex = currentIndex + 1;
        if (nextIndex < Math.ceil(videoCards.length / videosPerPage)) {
            setActiveVideo(nextIndex);
        } else {
            setActiveVideo(0); // Wrap around to the first set of videos
        }
    }

    // Function to show previous set of video cards
    function showPrevSet() {
        const prevIndex = currentIndex - 1;
        if (prevIndex >= 0) {
            setActiveVideo(prevIndex);
        } else {
            setActiveVideo(Math.ceil(videoCards.length / videosPerPage) - 1); // Wrap around to the last set of videos
        }
    }

    // Add event listeners to control buttons
    controlBtns.forEach(btn => {
        btn.addEventListener("click", function() {
            if (this.classList.contains("fa-angle-left")) {
                showPrevSet();
            } else if (this.classList.contains("fa-angle-right")) {
                showNextSet();
            }
        });
    });

    // Initialize active slide
    setActiveVideo(currentIndex);
});
