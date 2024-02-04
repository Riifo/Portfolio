#include <iostream>
#include <vector>
#include <string>

using namespace std;

//CarDealership::CarDealership() //constructor
//{
//}

// Customers
class Customer {
public:
    Customer(string name, string phone) {
        this->name = name;
        this->phone = phone;
    }
    string getName() { return name; }
    string getPhone() { return phone; }
private:
    string name;
    string phone;
};

// Employees
class Employee {
public:
    Employee(string name, string role) {
        this->name = name;
        this->role = role;
    }
    string getName() { return name; }
    string getRole() { return role; }
private:
    string name;
    string role;
};

// Cars
class Car {
public:
    Car(string make, string model, int year) {
        this->make = make;
        this->model = model;
        this->year = year;
    }
    string getMake() { return make; }
    string getModel() { return model; }
    int getYear() { return year; }
private:
    string make;
    string model;
    int year;
};

// CarDealership
class CarDealership {
public:
    void addCar(string make, string model, int year) { //adding car
        Car car(make, model, year);
        cars.push_back(car);
    }
    void addCustomer(string name, string phone) { //adding customer
        Customer customer(name, phone);
        customers.push_back(customer);
    }
    void addEmployee(string name, string role) { //adding employee
        Employee employee(name, role);
        employees.push_back(employee);
    }
    void sales() {
        cout << "Customers:" << endl; //gets customer data
        for (int i = 0; i < customers.size(); i++) {
            cout << customers[i].getName() << " (" << customers[i].getPhone() << ")" << endl;
        }
        cout << "Employees:" << endl; //gets employee data
        for (int i = 0; i < employees.size(); i++) {
            cout << employees[i].getName() << " (" << employees[i].getRole() << ")" << endl;
        }
    }
private:
    vector<Car> cars;
    vector<Customer> customers;
    vector<Employee> employees;
};



//void CarDealership::addCar(string maker, string model, int year) //adding car
//{
//    Car newCar(maker, model, year); //creates car object
//    cars.push_back(newCar); //adds car to dealership
//}

//void CarDealership::listCars() //list cars in dealership
//{
//    for (int i = 0; i < cars.size(); i++)
//    {
//        cout << cars[i].getMaker() << " " << cars[i].getModel() << " (" << cars[i].getYear() << ")" << endl;
//    }
//}


//Return your project with at least a few objects created for each class. Use a sales function and show customer data and a function with employee data.
//Use polymorphism in at least one class, use an abstract class. grades = 1 to 3
//Use inherit , abstract class, polymorphism  make your program works in the function main () = 5  (buy car, costumer info)