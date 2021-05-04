#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverse the list
 * @h: head of list
 *
 * Return: reversed list
 */
listint_t *reverse_list(listint_t **h)
{
	listint_t *tmp1, *tmp2, *tmp3;

	tmp1 = *h;
	tmp2 = NULL;

	while (tmp1)
	{
		tmp3 = tmp1->next;
		tmp1->next = tmp2;
		tmp2 = tmp1;
		tmp1 = tmp3;
	}
	*h = tmp2;
	return (*h);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1, *tmp2;
	int nodes, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp1 = *head;
	for (nodes = 0; tmp1; nodes++)
		tmp1 = tmp1->next;

	tmp1 = *head;
	tmp2 = reverse_list(&tmp1);

	for (i = 0; i < nodes; i++)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	return (1);
}
