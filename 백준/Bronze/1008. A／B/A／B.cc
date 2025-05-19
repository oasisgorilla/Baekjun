#include <iostream>
#include <iomanip>

int main()
{
    float x;
    float y;
    
    std::cin >> x >> y;
    std::cout << std::fixed << std::setprecision(10) <<  (double)x / y;

    return 0;
}