#include "lists.h"
#include <stdio.h>
/**
 */
int is_palindrome(listint_t **head)
{
	int i = 0, x = 0, s = 0;
	listint_t *tmp = *head, *tmp2 = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp->next->next)
	{
		tmp = tmp->next;
		i++;
	}
	s = i / 2;
	if (i % 2 != 0)
		x--;
	for (; x < s + 1; x++)
	{
		tmp = *head;
		for (i = s * 2; i - x != 0; i--)
		{
			tmp = tmp->next;
		}
		if (tmp->next->n != tmp2->n)
		{
			return (0);
		}
		tmp2 = tmp2->next;
	}
	return (1);
}
