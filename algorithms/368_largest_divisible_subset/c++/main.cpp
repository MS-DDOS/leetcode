#include <iostream>
#include <vector>
#include "Solution.hpp"

int main(int argc, char ** argv){
	std::vector<int> v = {1, 2, 4, 5, 6};
	Solution s;
	std::vector<int> r = s.largestDivisibleSubset(v);
	for(int i : r) {
		std::cout << i << std::endl;
	}
	return 0;
}