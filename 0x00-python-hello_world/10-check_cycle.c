#include "lists.h"

/**
 * check_cycle - Checks for cycle
 *
 * @list: Linked list
 *
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	if (!list || !list->next)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
