#include <stdio.h>
#include <stdlib.h>

// Define the structure for a tree node
struct node {
    int content;
    struct node *left;
    struct node *right;
};

// Function to create a new node
struct node *newnode(int c) {
    struct node *temp = malloc(sizeof(struct node));
    temp->content = c;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

// Function to insert a node into the binary tree
struct node *insert(struct node *root, int c) {
    if (root == NULL) {
        return newnode(c);
    }
    if (c < root->content) {
        root->left = insert(root->left, c);
    } else {
        root->right = insert(root->right, c);
    }
    return root;
}

// Function to print the tree in in-order traversal
void printinorder(struct node *root) {
    if (root != NULL) {
        printinorder(root->left);
        printf("%d ", root->content);
        printinorder(root->right);
    }
}

// Function to count the number of nodes in the tree
int countnodes(struct node *root) {
    if (root == NULL) {
        return 0;
    }
    return 1 + countnodes(root->left) + countnodes(root->right);
}

// Function to calculate the sum of the nodes' contents
int sumnodes(struct node *root) {
    if (root == NULL) {
        return 0;
    }
    return root->content + sumnodes(root->left) + sumnodes(root->right);
}

// Function to find the node with the minimum value (iterative approach)
struct node *findminimum(struct node *root) {
    if (root == NULL) {
        return NULL;
    }
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Function to delete all nodes in the tree
struct node *deletetree(struct node *root) {
    if (root != NULL) {
        // Delete left and right subtrees first
        root->left = deletetree(root->left);
        root->right = deletetree(root->right);

        // Print the deleted node
        printf("Deleting node with value: %d\n", root->content);

        // Free the memory of the current node
        free(root);
    }
    return NULL;
}

// Main function to test the tree operations
int main() {
    struct node *root = NULL;

    // Insert nodes into the tree
    root = insert(root, 12);
    root = insert(root, 5);
    root = insert(root, 15);
    root = insert(root, 3);
    root = insert(root, 10);

    // Print the tree in in-order traversal
    printf("In Order Display:\n");
    printinorder(root);
    printf("\n");

    // Count and print the number of nodes
    printf("The number of nodes in the tree: %d\n", countnodes(root));

    // Calculate and print the sum of the nodes' contents
    printf("Sum of the contents in the tree: %d\n", sumnodes(root));

    // Find and print the minimum value in the tree
    struct node *minNode = findminimum(root);
    if (minNode != NULL) {
        printf("Minimum value in a node: %d\n", minNode->content);
    }

    // Delete all nodes in the tree
    printf("Deleting all nodes of the tree:\n");
    root = deletetree(root);

    return 0;
}
