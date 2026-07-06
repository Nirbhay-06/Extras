#include<iostream>

int main(){

    double a , b;
    char operation;

    std::cout << "Enter the firt number: ";
    std::cin >> a;

    std::cout << "Enter the second number: ";
    std::cin >> b;

    std::cout << "Enter the operation(+,-,*,/,%): ";
    std::cin >> operation;

    switch(operation){
        case '+':
            std::cout << "The addition is " << (a + b) ;
            break;
        
        case '-':
            std::cout << "The subtraction is " << (a - b);
            break;
        
        case '*':
            std::cout << "The Multiplication is " << (a * b);
            break;

        case '/':
            if(b != 0){
                std::cout << "The Division is " << (a / b);
            }
            else{
                std::cout << "Not divisible by zero.";
            }
            break;

        case '%':
            if(b != 0){
                std::cout << "The remainder is " << (int(a) % int(b));
            }
            else{
                std::cout << "Not divisible by zero.";
            }
            
            break;

        default:
            std::cout << "Invalid Operation";
            break;
    }

    return 0;
}