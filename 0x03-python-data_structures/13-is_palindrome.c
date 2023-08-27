#include "lists.h"

/**
 * palindrome_recursive - check for palindrome in a recursive manner.
 * @head: pointer to the first node of a listint_t list, passed by
 * value.
 * @head2: the same as @head but passed by reference
 * Description: check if a listint_t singly linked list read the
 * the same forward as its backward.
 * Helper function to is_palindrome.
 * Return: 1 (True) 0 (False)
 */
int palindrome_recursive(listint_t *head, listint_t **head2)
{
	int result;

	if (head == NULL)
		return (1);

	result = palindrome_recursive(head->next, head2);

	if (head->n != (*head2)->n)
		return (0);

	*head2 = (*head2)->next;

	return (result);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node of a listint_t singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;

	current = *head;
	return (palindrome_recursive(*head, &current));
}
