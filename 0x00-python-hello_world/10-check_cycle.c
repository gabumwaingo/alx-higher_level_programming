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
	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
