$(document).ready(function () {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	$.get(url, sayHello(data));
});


function sayHello(data) {
	if (data.hello & data.hello.length > 1) {
		$('div#hello').text(data.hello);
	}
}
