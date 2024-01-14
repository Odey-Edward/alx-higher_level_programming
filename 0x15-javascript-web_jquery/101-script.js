$(function () {
	const add_item = $('div#add_item');
	const remove_item = $('div#remove_item');
	const clear_list = $('div#clear_list');
	const element = $('ul.my_list');

	add_item.click(function () {
		element.append('<li>Item</li>');
	});

	remove_item.click(function () {
		element.remove();
	});

	clear_list.click(function () {
		element.empty();
	});
});
