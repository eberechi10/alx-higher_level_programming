#include "lists.h"
#include <unistd.h>
#include <stdlib.h>

/**
 * insert_node - a function to inserts a node into ordered list
 *
 * @head: pointer of the node
 * @number: node to insert.
 *
 * Return: if succuss address node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head;
	listint_t *x;
	listint_t *node;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		node->next = *head;
		return (*head = node);
	}
	else
	{
		while (i && i->n < number)
		{
			x = i;
			i = i->next;
		}

		x->next = node;
		node->next = i;
	}

	return (node);
}
