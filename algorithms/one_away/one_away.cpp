#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool one_away(std::string, std::string);

int main(int argc, char ** argv){
	std::vector< std::pair < std::string, std::string > > v;
	v.push_back(std::pair<std::string, std::string>("pale","ple"));
	v.push_back(std::pair<std::string, std::string>("zale","zales"));
	v.push_back(std::pair<std::string, std::string>("pale","bale"));
	v.push_back(std::pair<std::string, std::string>("pale","bake"));
	for(auto i : v){
		std::cout << one_away(i.first, i.second) << std::endl;
	}
	return 0;
}

bool one_away(std::string input_string, std::string comparison_string){
	if(abs(input_string.size() - comparison_string.size()) > 1)
		return false;

	short loffset = 0;
	short roffset = 0;
	bool incorrect = false;
	for(int i = 0; i < std::min(input_string.size(), comparison_string.size()); i++) {
		if(input_string[i + loffset] != comparison_string[i + roffset]){
			if(input_string.size() < comparison_string.size())
				loffset--;
			else if(input_string.size() > comparison_string.size())
				roffset--;

			if(incorrect)
				return false;
			else
				incorrect = true;
		}
		if((incorrect == true) && (input_string.back() != comparison_string.back()))
			return false;
	}
	return true;
}