#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		if ((*head)->n > new->n)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		while (current != NULL)
		{
			if (current->next->n > new->n)
			{
				temp = current->next;
				current->next = new;
				new->next = temp;
				return (new);

			}
			current = current->next;
		}
		current = new;
	}
	return (new);
}
