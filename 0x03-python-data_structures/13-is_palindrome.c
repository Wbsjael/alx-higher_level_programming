#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int array[2048], i = 0, j;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (array[j] != array[i - j - 1])
			return (0);
	}

	return (1);
}
