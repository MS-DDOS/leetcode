#include <iostream>

struct node{
	int val;
	struct node* next;
};

void push(struct node **, int);
void print_list(struct node *);
void reverse_list(struct node **);

int main(int argc, char ** argv){
	node * list = NULL;
	push(&list, 4);
	push(&list, 3);
	push(&list, 2);
	push(&list, 1);

	print_list(list);
	reverse_list(&list);
	print_list(list);

}

void reverse_list(struct node ** head_ref){
	struct node * previous = NULL;
	struct node * curr = *head_ref;
	while(curr != NULL){
		struct node * next = curr->next;
		curr->next = previous;
		previous = curr;
		curr = next;
	}
	*head_ref = previous;
}

void push(struct node ** head_ref, int data) {
	struct node * new_node = (struct node*)malloc(sizeof(struct node));
	
	new_node->val = data;
	new_node->next = *head_ref; //deref since its by reference
	*head_ref = new_node;
}

void print_list(struct node * head_ref){
	struct node * ref = head_ref;
	while(ref != NULL){
		std::cout << ref->val << std::endl;
		ref = ref->next;
	}
}