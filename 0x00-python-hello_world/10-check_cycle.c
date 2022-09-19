#include "lists.h"
/**
 * check_cycle - checks for a cycle in linked lists
 * @list: pointer to the linked list
 * Return: 0 no cycle 1 there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *S = list, *F = list;

	while (S && F && F->next)
	{
		S = S->next;
		F = F->next->next;
		if (F == S)
		{
			return (1);
		}
	}
	return (0);
}
