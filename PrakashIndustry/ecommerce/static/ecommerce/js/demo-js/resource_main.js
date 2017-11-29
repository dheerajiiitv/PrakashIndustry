/**
 * main.js
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 * 
 * Copyright 2016, Codrops
 * http://www.codrops.com
 */
;(function(window) {

	'use strict';

	function init() {
		[].slice.call(document.querySelectorAll('.nav')).forEach(function(nav) {
			var navItems = [].slice.call(nav.querySelectorAll('.nav__item')),
				itemsTotal = navItems.length,
				setCurrent = function(item) {
					// return if already current
					if( item.classList.contains('nav__item--current') ) {
						return false;
					}
					// remove current
					var currentItem = nav.querySelector('.nav__item--current');
					currentItem.classList.remove('nav__item--current');
					
					// set current
					item.classList.add('nav__item--current');
				};
			
			navItems.forEach(function(item) {
				item.addEventListener('click', function() { setCurrent(item); });
			});
		});

		[].slice.call(document.querySelectorAll('.link-copy')).forEach(function(link) {
			link.setAttribute('data-clipboard-text', location.protocol + '//' + location.host + location.pathname + '#' + link.parentNode.id);
			new Clipboard(link);
			link.addEventListener('click', function() {
				link.classList.add('link-copy--animate');
				setTimeout(function() {
					link.classList.remove('link-copy--animate');
				}, 300);
			});
		});
	}

	init();

})(window);

jQuery('.targetDiv').hide();
			jQuery(function(){
        	jQuery('.showSingle').click(function(){
              jQuery('.targetDiv').hide();
              
              jQuery('#div'+$(this).attr('target')).show();
              jQuery('#div'+$(this).attr('target')).addClass('fadeIn animated');
              // jQuery('.targetDiv').addClass('slideOutUp animated');
        });
});
    	jQuery(function(){
        	jQuery('.showSingle').click(function(){
              jQuery('.targetDiv1').hide();
              // jQuery('.targetDiv1').addClass('slideOutUp animated');
             
        });
});	
    	jQuery(function(){
        	jQuery('.showSingle1').click(function(){
              jQuery('.targetDiv1').show();
              jQuery('.targetDiv1').addClass('fadeIn animated');
             jQuery('.targetDiv').hide();
             // jQuery('.targetDiv').addClass('fadeOutUp animated');
        });
});	

    	jQuery('.goaldiv').hide();
			jQuery(function(){
        	jQuery('.showbingle').click(function(){
              jQuery('.goaldiv').hide();
              
              jQuery('#Div'+$(this).attr('target')).show();
              jQuery('#Div'+$(this).attr('target')).addClass('fadeIn animated');
              // jQuery('.targetDiv').addClass('slideOutUp animated');
        });
});
			jQuery(function(){
        	jQuery('.showbingle').click(function(){
              jQuery('.goaldiv1').hide();
              // jQuery('.targetDiv1').addClass('slideOutUp animated');
             
        });
});	
			jQuery(function(){
        	jQuery('.showbingle1').click(function(){
              jQuery('.goaldiv1').show();
              jQuery('.goaldiv1').addClass('fadeIn animated');
             jQuery('.goaldiv').hide();
             // jQuery('.targetDiv').addClass('fadeOutUp animated');
        });
});	


 jQuery('.myslider-demo').hide();
      jQuery(function(){
          jQuery('.show-demo').click(function(){
          	
              jQuery('.myslider-demo').hide();

              jQuery('#div'+$(this).attr('target')).show();
              jQuery('#div'+$(this).attr('target')).addClass('fadeIn animated');
              // jQuery('.targetDiv').addClass('slideOutUp animated');
        });
});

jQuery(function(){
          jQuery('.show-demo').click(function(){
              jQuery('.myslider-demo1').hide();
              
              // jQuery('.targetDiv1').addClass('slideOutUp animated');
             
        });
}); 

jQuery(function(){
          jQuery('.show-demo1').click(function(){
              jQuery('.myslider-demo1').show();
              jQuery('.myslider-demo1').addClass('fadeIn animated');
             jQuery('.myslider-demo').hide();
             // jQuery('.targetDiv').addClass('fadeOutUp animated');
        });
}); 