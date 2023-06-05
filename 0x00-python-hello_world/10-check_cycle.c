#include "lists.h"

/**
 *check_cycle - function to check for cycle in linked list
 *
 *@list: the list to check.
 *
 *Return: if success 1, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;


	if (!list || !list->next)
		return (0);

	fast = list->next;
	slow = list;

	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);

	}
	return (0);
}
