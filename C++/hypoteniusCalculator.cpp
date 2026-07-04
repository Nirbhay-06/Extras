#include<iostream>
#include<cmath>


int main(){

    double height,base,hypotenous;

    std::cout << "Enter the Height of triangle: ";
    std::cin >> height;

    std::cout << "Enter the Base of the Triangle: ";
    std::cin >> base;

    hypotenous = sqrt(pow(height, 2) + pow(base, 2));

    std::cout << "The Hypotenous of the given Triangle is" << hypotenous;
    

    return 0;
}