$(document).ready(function () {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
		if (data.result && data.result.length > 1) {
			$.each(data.result, function(index, movies) {
				$('ul#list_movies').append('<li>' + movies.tittle + '</li>');
			});
		}
	});
});
