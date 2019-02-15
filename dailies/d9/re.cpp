#include "re.h"
#include <boost/any.hpp>
#include <vector>
#include <string>
#include <iostream>

typedef std::vector<boost::any> Regex;
bool match(std::string s, Regex re){
	// If for each obj in Regex, check is true
	// Then return true
	// Else return false
}
int main(){
	Regex re;
	plus p("who");
	std::cout << p.str << std::endl;

	return 0;
}
