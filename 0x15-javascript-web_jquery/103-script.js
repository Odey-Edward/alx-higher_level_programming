$(function () {
	const langCode = $('INPUT#language_code').val();

	$('INPUT#btn_translate').click(function () {

		$.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data) {
			if (data.hello)
			{
				$('div#hello').text(data.hello);
			}
		});
	});

	$('input#language_code').keypress(function(event) {
		if (event.which === 13) {
			$.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data) {
				if (data.hello)
				{
					$('div#hello').text(data.hello);
				}
			});

			event.preventDefault();
		}

	});
});
