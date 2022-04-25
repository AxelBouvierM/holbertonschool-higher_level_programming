#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = NULL, *second = NULL;

	first = list;
	second = list;
	if (list == NULL)
		return (0);
	second = second->next;
	while (second != NULL && second->next != NULL)
	{
		if (first == second)
			return (1);
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
