// Forward declaration of isBadVersion API
bool isBadVersion(int version);

class Solution {
	public:
		int firstBadVersion(int n){
			int low = 1;
			int high = n;
			while(low <= high){
				int mid = low + ((high-low)/2);
				bool bad = isBadVersion(mid);
				if(bad){
					if(!isBadVersion(mid-1))
						return mid;
					else
						high = mid-1;
				} else {
					low = mid + 1;
				}
			}
			return -1;
		}
};
