#include <iostream>
#include <cstring>
#include <vector>

char* urlify(char*);

int main(int argc, char ** argv) {
	char x[] = "please urlify this string now urlify this!";
	char * y = urlify(x);
	std::cout << x << std::endl;
	std::cout << y << std::endl;
	delete[] y;
	return 0;
}

char * urlify(char * input){
	std::vector<int> * space_idx = new std::vector<int>();
	int input_len = strlen(input);
	for(int i = 0; i < input_len; i++){
		if(input[i] == ' ')
			space_idx->push_back(i);
	}
	int new_len = input_len + (space_idx->size()*2) + 1; //make room for additional characters and null terminator
	char * urlified = new char[new_len];
	urlified[new_len] = '\0';
	std::vector<int>::iterator s = space_idx->begin();
	int offset = 0;
	for(int i = 0; i < input_len; i++){
		if(i == *s){
			urlified[i + offset] = '%';
			urlified[i + offset + 1] = '2';
			urlified[i + offset + 2] = '0';
			offset += 2;
			s++;
		}
		if(input[i] != ' ')
			urlified[i + offset] = input[i];
	}
	delete space_idx;
	return urlified;
}
