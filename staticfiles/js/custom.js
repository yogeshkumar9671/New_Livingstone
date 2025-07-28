/* JS Document */

/******************************

[Table of Contents]



******************************/

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var header = $('.header');
	var menuActive = false;
	var menu = $('.menu');
	var burger = $('.burger_container');

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initHomeSlider();
	initMenu();
	initGallery();
	initTestSlider();
	initLightbox();

	/* 




	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 100)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/* 




	3. Init Menu

	*/

	function initMenu()
	{
		if($('.menu').length)
		{
			var menu = $('.menu');
			if($('.burger_container').length)
			{
				burger.on('click', function()
				{
					if(menuActive)
					{
						closeMenu();
					}
					else
					{
						openMenu();

						$(document).one('click', function cls(e)
						{
							if($(e.target).hasClass('menu_mm'))
							{
								$(document).one('click', cls);
							}
							else
							{
								closeMenu();
							}
						});
					}
				});
			}
		}
	}

	function openMenu()
	{
		menu.addClass('active');
		menuActive = true;
	}

	function closeMenu()
	{
		menu.removeClass('active');
		menuActive = false;
	}

	/* 

	4. Init Home Slider

	*/

	function initHomeSlider()
	{
		if($('.home_slider').length)
		{
			var homeSlider = $('.home_slider');

			homeSlider.owlCarousel(
			{
				items:1,
				autoplay:true,
				loop:true,
				nav:false,
				smartSpeed:1200
			});

			// Custom Navigation
			if($('.home_slider_next').length)
			{
				var next = $('.home_slider_next');
				next.on('click', function()
				{
					homeSlider.trigger('next.owl.carousel');
				});
			}

			/* Custom dots events */
			if($('.home_slider_custom_dot').length)
			{
				$('.home_slider_custom_dot').on('click', function(ev)
				{	
					var dot = $(ev.target);
					$('.home_slider_custom_dot').removeClass('active');
					dot.addClass('active');
					homeSlider.trigger('to.owl.carousel', [$(this).index(), 300]);
				});
			}

			/* Change active class for dots when slide changes by nav or touch */
			homeSlider.on('changed.owl.carousel', function(event)
			{
				$('.home_slider_custom_dot').removeClass('active');
				$('.home_slider_custom_dots li').eq(event.page.index).addClass('active');
			});	
		}
	}

	/* 

	5. Init Gallery

	*/

	function initGallery()
	{
		if($('.gallery_slider').length)
		{
			var gallerySlider = $('.gallery_slider');
			gallerySlider.owlCarousel(
			{
				items:6,
				loop:true,
				margin:22,
				autoplay:true,
				nav:false,
				dots:false,
				responsive:
				{
					0:
					{
						margin:7,
						items:3
					},
					575:
					{
						margin:7,
						items:6
					},
					991:
					{
						margin:22,
						items:6
					}
				}
			});
		}
	}

	/* 

	6. Init Testimonials Slider

	*/

	function initTestSlider()
	{
		if($('.test_slider').length)
		{
			var testSlider = $('.test_slider');
			testSlider.owlCarousel(
			{
				items:1,
				loop:true,
				autoplay:true,
				smartSpeed:1200,
				nav:false,
				dots:false
			});
		}
	}

	/*

	7. Init Lightbox

	*/

	function initLightbox()
	{
		if($('.gallery_item').length)
		{
			$('.colorbox').colorbox(
			{
				rel:'colorbox',
				photo: true,
				maxWidth:'95%',
				maxHeight:'95%'
			});
		}
	}
});









// new added js from cart scroll
function scrollGrid(direction) {
  const grid = document.getElementById("exploreGrid");
  const scrollAmount = 320; // Width to scroll by
  grid.scrollBy({
    left: direction * scrollAmount,
    behavior: 'smooth'
  });
}



// new cart function
const track = document.getElementById('carouselTrack');
const slides = document.querySelectorAll('.slide');
const pagination = document.getElementById('pagination');
const pauseBtn = document.getElementById('pauseBtn');

let index = 0;
let autoSlide = true;
let slideInterval = setInterval(() => {
  if (autoSlide) nextSlide();
}, 3000);

function updateSlidePosition() {
  track.style.transform = `translateX(-${index * 100}%)`;
  pagination.innerText = `${index + 1} / ${slides.length}`;
}

function nextSlide() {
  index = (index + 1) % slides.length;
  updateSlidePosition();
}

function prevSlide() {
  index = (index - 1 + slides.length) % slides.length;
  updateSlidePosition();
}

function toggleAutoSlide() {
  autoSlide = !autoSlide;
  pauseBtn.innerText = autoSlide ? '⏸' : '▶️';
}






function scrollSlider(direction) {
  const slider = document.getElementById('slider');
  const scrollAmount = 320;
  slider.scrollBy({
    left: direction * scrollAmount,
    behavior: 'smooth'
  });
}



// home page cart icon js for product count

  function updateCartIcon() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartIcon = document.querySelector(".cart_num");
    if (cartIcon) {
      cartIcon.textContent = totalCount;
    }
  }

  window.addEventListener("DOMContentLoaded", updateCartIcon);




// wishlist count


function updateWishlistCount() {
    const wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];
    const countElement = document.getElementById("wishlistCount");
    if (countElement) {
      countElement.textContent = wishlist.length;
    }
  }

  document.addEventListener("DOMContentLoaded", updateWishlistCount);




// nav bar avatar to sigh in and sign up


  
  document.addEventListener('DOMContentLoaded', function () {
    const wrapper = document.querySelector('.avatar-dropdown-wrapper');
    const avatar = wrapper.querySelector('.avatar');

    // Only toggle on avatar click
    avatar.addEventListener('click', function (e) {
      e.stopPropagation(); // Prevent bubbling to document
      wrapper.classList.toggle('active');
    });

    // Click anywhere outside closes the dropdown
    document.addEventListener('click', function (e) {
      if (!wrapper.contains(e.target)) {
        wrapper.classList.remove('active');
      }
    });
  });








