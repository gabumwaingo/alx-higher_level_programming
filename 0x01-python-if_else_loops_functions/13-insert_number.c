#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - inserts nmber in a sorted list
 * @head: pointer to the first node of the list
 * @number: the number to be inserted in the list
 * Return: address of new node or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	new->n = number;

	if (*head == NULL)
		return (NULL);

	current = *head;

	if ((current->n) >= new->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while ((current->next != NULL) && (current->next->n < new->n))
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
