#include "lists.h"
#include <stdio.h>
#include <unistd.h>

#define MAXLIST 50

int check_cycle(listint_t *list)
{
	int i;
	char *addresses[MAXLIST];
	listint_t *current;

	for (i = 0; i < MAXLIST; i++)
		addresses[i] = NULL;

	current = list;
	while (current != NULL)
	{
		i = 0;
		while (addresses[i] != NULL)
		{
			if ((char *)current == addresses[i])
				return (1);
			i++;
		}
		addresses[i] = (char *)current;
		current = current->next;
	}
	return (0);
}
