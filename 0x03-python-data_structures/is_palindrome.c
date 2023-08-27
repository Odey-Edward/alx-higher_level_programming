#include "lists.h"

/**
 * pop - remove the last node from a listint_t
 * singly linked list
 * @head: pionter to the first node in a listint_t
 * singly linked list
 * Return: the last node removed
 */
listint_t *pop(listint_t **head)
{
	listint_t *current, *last;

	if (!(*head))
		return (NULL);

	last = *head;

	while (last->next)
	{
		current = last;
		last = last->next;
	}

	if (current)
		current->next = NULL;

	return (last);
}

/**
 * add_last - creat a linked list of node romoved from the
 * the end of a listint_t linked list.
 * @last_head: pointer to the first node of all last node
 * in a listint_t linked list.
 * @last: the node to add to the list of last node
 * Return: @last_head
 */
listint_t *add_last(listint_t **last_head, listint_t *last)
{
	if (!(*last_head))
	{
		*last_head = last;
		return (*last_head);
	}

	last->next = *last_head;
	*last_head = last;

	return (*last_head);

}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node of a listint_t singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *last, *last_head = NULL;

	if (!(*head))
		return (1);

	current = *head;
	while (current->next)
	{
		last = pop(head);
		if (last->n != current->n)
		{
			last_head = add_last(&last_head, last);
			for (; current->next; )
				current = current->next;

			current->next = last_head;
			return (0);
		}

		last_head = add_last(&last_head, last);
		if (!current->next)
			break;

		current = current->next;
	}

	current->next = last_head;
	return (1);
}
