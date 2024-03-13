#include "lists.h"

/**
 * check_cycle - checks the existing cycle in linked list
 * @list : pointer to head of the linked list
 * Return: 0 if there is no cycle in the linked list else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *falcon;

	if (list == NULL || list->next == NULL)
		return (0);

	snail = list->next;
	falcon = list->next->next;

	while (snail && falcon && falcon->next)
	{
		if (snail == falcon)
			return (1);
		snail = snail->next;
		falcon = falcon->next->next;
	}
	return (0);
}
