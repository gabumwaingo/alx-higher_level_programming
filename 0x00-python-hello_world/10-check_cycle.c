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
	listint_t *fast, *slow;
	
	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = slow->next;

	while (slow != 0 && fast->next != 0 && fast->next->next!= 0)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;

	}
	return (0);
}
