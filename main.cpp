#include <iostream>
#include "CarDealership.cpp"

using namespace std;

int main()
{
    CarDealership dealership; //object
    
    dealership.addCar("Opel", "Cadet", 1980); //add car
    dealership.addCar("Toyota", "Prius", 1998);
    dealership.addCar("Mercedes Benz", "CL200", 1999);
    dealership.addCar("Ford", "Ranger", 2020);
    dealership.addCar("Ford", "Mustang", 1977);

    dealership.addEmployee("Roger Moore", "CEO"); //add employee
    dealership.addEmployee("Steven Strange", "Manager");
    dealership.addEmployee("Simon Cowel", "Salerperson");

    dealership.addCustomer("Rafael Nadal", "040-1445679"); //add customer
    dealership.addCustomer("Natalie Portman", "050-677880");

    dealership.sales();
    //dealership.listCars();

    return 0;
}


//Return your project with at least a few objects created for each class. Use a sales function and show customer data and a function with employee data.
//Use polymorphism in at least one class, use an abstract class. grades = 1 to 3
//Use inherit , abstract class, polymorphism  make your program works in the function main () = 5  (buy car, costumer info)