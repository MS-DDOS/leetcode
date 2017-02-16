#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        unordered_map<int, unordered_set<int> > buckets;
        buckets[-1] = unordered_set<int>();
        std::sort(nums.begin(), nums.end());
        for( auto x: nums){
        	vector<unordered_set<int> > * candidates = new vector<unordered_set<int> >();
        	for( auto items : buckets) {
        		if(x % items.first == 0){
        			candidates->push_back(buckets[items.first]);
        		}
        	}
        	buckets[x] = max_element(*candidates);
        	free(candidates);
        	buckets[x].insert(x);
        }

        unordered_set<int> longest = max_length_set(buckets);
        vector<int> output;
        std::copy(longest.begin(), longest.end(), std::back_inserter(output));

        return output;
    }

    unordered_set<int> max_element(vector<unordered_set<int> > collection){
    	if(collection.size() == 0) {
    		return unordered_set<int>();
    	}
    	unordered_set<int> max = collection[0];
    	for(auto item : collection){
    		if(item.size() > max.size()){
    			max = item;
    		}
    	}
    	return max;
    }

    unordered_set<int> max_length_set(unordered_map<int, unordered_set<int> > map){
    	unordered_set<int> longest;
    	for(auto s: map){
    		if(s.second.size() > longest.size()) {
    			longest = s.second;
    		}
    	}
    	return longest;
    }

    void printMap(unordered_map<int, unordered_set<int> > buckets){
    	for(auto p : buckets){
    		std::cout << p.first << "-> ";
    		for(auto s: p.second){
    			std::cout << s << ",";
    		} 
    		cout << std::endl;
    	}
    }

    ~Solution(){

    }
};