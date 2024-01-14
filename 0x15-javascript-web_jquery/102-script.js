$(function () {
	$('input#language_code').click(function () {
		const langCode = $('INPUT#language_code').val()
		$.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data) {
			if (data.hello)
			{
				$('div#hello').text(data.hello);
			}
		});
	});
});
