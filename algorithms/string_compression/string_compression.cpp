#include <iostream>
#include <stack>
#include <string>
#include <sstream>

//This program is a C++ implemenation of the string compression algorithm.

std::string compress(std::string);

int main(int argc, char ** argv){
	std::cout << compress(argv[1]) << std::endl;
	return 0;
}

std::string compress(std::string input){
	std::stringstream output_ss;
	std::stack<char> * stack = new std::stack<char>();

	for(char c : input){
		if(stack->size() > 0){
			if(c == stack->top()) { //stack.peek()
				stack->push(c);
			} else {
				output_ss << stack->top() << stack->size();
				delete stack;
				stack = new std::stack<char>();
				stack->push(c);
			}
		} else {
			stack->push(c);
		}
	}
	if(stack->size() > 0){
		output_ss << stack->top() << stack->size();
	}
	delete stack;
	return output_ss.str();
}