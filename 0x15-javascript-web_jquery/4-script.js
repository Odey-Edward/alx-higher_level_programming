$('div#toggle_header').click(function () {
	const sender = $('header');

	if (sender.hasClass('green')) {
		sender.removeClass('green');
		sender.addClass('red');
	} else {
		sender.removeClass('red');
		sender.addClass('green');
	}
});
