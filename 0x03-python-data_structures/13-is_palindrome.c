#include "lists.h"

/**
 * check_palindrome - It check the list for palindrome
 *
 * @head: the head pointer of the list.
 * @last: the pointer of the end of the list.
 *
 * Return: success if 0, otherwise 1.
 */
int check_palindrome(listint_t **head, listint_t *end)
{
	if (!end)
		return (1);

	if (check_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}


/**
 * is_palindrome - function to call check_palindrome to check palindrome
 *
 * @head: the pointer the list
 *
 * Return: if success 0, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	return (check_palindrome(head, *head));
}
