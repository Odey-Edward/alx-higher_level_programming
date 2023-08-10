#include "lists.h"

/**
 * check_cycle - check for a cycle in a linked list
 * @list: head of a link list
 * Return: 1(Detect a cycle) 0(No cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
