#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts node
 *
 * @head: Head
 * @number: data
 *
 * Return: Address of new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!temp || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (temp && temp->next && temp->next->n < number)
			temp = temp->next;

		new_node->next = temp->next;
		temp->next = new_node;
	}
	return (new_node);
}
