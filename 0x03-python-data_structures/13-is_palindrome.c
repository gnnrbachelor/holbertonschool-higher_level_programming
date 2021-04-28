#include "lists.h"

/**
 * reverse_linked - Reverses linked list
 *
 * @head: head node
 * Return: Pointer to head
 */

listint_t *reverse_linked(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks for palindrome
 * @head: address
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *turtle = *head;
	listint_t *hare = *head;
	listint_t *original = *head;
	listint_t *reversed = NULL;

	if (head)
	{
		while (hare && hare->next)
		{
			turtle = turtle->next;
			hare = hare->next->next;
		}
		reversed = reverse_linked(&turtle);

		while (reversed)
		{
			if (original->n == reversed->n)
			{
				original = original->next;
				reversed = reversed->next;
			}
			else
				return (0);
		}
	}
	return (1);
}

