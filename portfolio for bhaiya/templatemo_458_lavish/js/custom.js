
//
$(document).ready(function() {
			$('#fullpage').fullpage({
				'verticalCentered': true,
				'scrollingSpeed': 400,
				'autoScrolling': false,
				'css3': true,
				'navigation': false,
				'navigationPosition': 'right',
			});
		});

// wow
$(function()
{
    new WOW().init();
    $(".rotate").textrotator();
})