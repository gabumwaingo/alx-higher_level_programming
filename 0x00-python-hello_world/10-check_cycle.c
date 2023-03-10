#include "list.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks whether a singly linked
 * list has a cycle
 * @list: pointer to head node
 * Return: 0 if no cycle 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *check = list;

	while (current && check && check->next)
	{
		current = current->next;
		check = check->next->next;

		if (current == check)
		{
			return (1);
		}
	}
	return (0);
}
