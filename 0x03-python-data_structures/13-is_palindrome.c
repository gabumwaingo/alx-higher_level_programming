#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

bool isPalindromeUtil(struct node** left,struct node* right)
{
    // Stop recursion when right
    if (right == NULL)
        return true;

    // If sub-list is not palindrome then
    // no need to check for current left
    // and right, return false
    bool isp = isPalindromeUtil(left,
                                right->next);
    if (isp == false)
        return false;

    // Check values at current left and right
    bool isp1 = (right->data == (*left)->data);

    // Move left to next node
    *left = (*left)->next;

    return isp1;
}

// A wrapper over isPalindromeUtil()
bool isPalindrome(struct node* head)
{
    isPalindromeUtil(&head, head);
}

// Push a node to linked list.
// Note that this function changes
// the head
void push(struct node** head_ref,
          char new_data)
{
    // Allocate node
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    // Put in the data
    new_node->data = new_data;

    // Link the old list off the new node
    new_node->next = (*head_ref);

    // Move the head to point to the new node
    (*head_ref) = new_node;
}

// A utility function to print a
// given linked list
void printList(struct node* ptr)
{
    while (ptr != NULL)
    {
        printf("%c->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}
