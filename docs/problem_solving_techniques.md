# Problem-Solving Techniques

## 2 Fundamental Problem-Solving Techniques

* Data Abstraction (wall) - isolates and hidse the implementation details of a module from the rest of the program (much as a wall can isolate and hide you from your neighbor)

* Recursion (mirror) - a repetitive technique that solves a problem by solving smaller problems of the exact same type (much like images in facing mirrors grow smaller with each reflection)

# Software Engineering and Object-Oriented Design

Software engineering is a branch of computer science that provides techniques to facilitate the developmet of computer programs.

# Problem-Solving

Problem-solving is the entire process of taking the statement of a problem and developing a computer program that solves that problem. 

* Gain an understanding of the problem to be solved
* Desing a conceptual solution
* Implement the solution as a computer program

## Object-oriented analysis and design (OOA/D)

From an object-oriented perspective, a solution is a computer program consisting of a system of interacting classes of objects.

Object-oriented analysis and design echniques help us to discover and describe objects and classes.

An object has a set of characteristics and behaviors related to the solution. Each object is responsible for some aspect of the solution. 

A class is a set of objects of the same type.

### Aspects of an object-oriented solution

A solution consists of modules.

#### Modules are self-contained units of code. A module can be one of the following:

* a single, stand-alone function
* a method of a class
* a class
* several functions or class that work closely together
* other blocks of code

Functions and methods implement algorithms.

An algorithm is a step-by-step recipe for performing a task within a finite period of time. Algorithms usually operate on a collection of data.

## Abstraction and Information Hiding

Each module is a box that states **what it does** and not how it does it.

No one box may "know" how any other box performs its task---it may only know what that task is.

### Abstraction separates the purpose of a module from its implementation

#### Modularity breaks a solution into modules; abstraction specifies each module clearly before implementation in a programming language

* What does a module assume and what action does it take?
* For what task is this module responsible when called on?

### Functional/Procedural abstraction separate the purpose of a module from its implementation

Once a module is written, you can use it without knowing the particulars of its algorithm as long as you have a staement of its purpose and description of its arguments. 

### Data abstraction applies to a collection of data and a set of operations on the data; it focuses on what the operations do instead of on how you will implement them. 

To focus on what operations to perform on data and not on how the data is stored, an abstract data type (ADT) should be defined. 

#### An Abstract Data Type (ADT) is a collection of data and a set of operations on the data

The operations can be used if their specs are know without knowing how the operations are implementated or how the data is stored. 

ADTs are implemented with data structures

## Principles of OOP

OOP languages allow us to build classes of objects. 

A class combines the attributes/characteristics of objects into a single type together with the objects' operations/behaviors into a single unit.

Attributes are typically data and the behaviors often operate on that data. 

Encapsulation is a technique that hides inner details.

Functions encapsulate behavior; objects encapsulate data and behavior. 

Inheritance allows you to reuse classes that you defined earlier---perhaps for differnt but related purposes---with appropriate modification.

Polymorphism allows the outcome of a particular operation to depend on the objects on which the operation acts. 