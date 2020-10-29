# Designing & Analyzing Algorithms

## Definition of Algorithm

An algorithm is a sequence of computational steps that transform input into output.

An algorithm is a tool for solving a well-specified computational problem.

The problem specifies the desired input/output relationship. 

The algorithm describes a computational procedure for achieving that input/output relationship.

Analogy: an algorithm is a thought plan

## Definition of Data Structure

A data structure is a way to store and organize data in order to facilitate access and modifications.

Data structures are manipulated by algorithms.

Algorithms may require several different types of operations to be performed on a data structure.

No single data strcutres works well for all purposes.

It is important to know the strengths and limitations of several of them.

Analogy: a data structure is a memory structure.

## Computer Resources: Time and Memory Space

Computing time and memory space are bounded resources.

Algorithms should be efficient in terms of time and memory space.

Total computer system performance depends on choosing efficient algorithms as much as choosing fast hardware.

Analogy: How much memory does a thought plan need? How much time does a thought plan need? What kind of memory structure does a thought plan need?

## Analyzing Algorithms

Analyzing an algorithm means predicting the resources that the algorithm requires.

Different algorithms devised to solve the same problem often differ dramatically in their efficiency.

By analyzing several candidate algorithms for a problem, we can identify a most efficient one.

## Data Structures are Dynamic Sets

A set is a well-defined collection of objects.

A set is also considered an object.

A dynamic set grows, shrinks, or otherwise changes over time when manipulated by algorithms.

The implemention of a dynamic set depends on the operations that it must support. 

## Elements of a Data Structure

The objects that make up a set are called elements or members.

The elements can be anything: numbers, people, letters of the alphabet, or other sets.

The attributes of elements can be examined and manipulated.

Some kinds of data structures assume that one of the element's attribues is an identifying key.

## Data Structure Operations

Two Types of Data Structure Operations:

1. Queries - return info about the data structure

2. Modifying - change the data structure

### CREATE ()

CREATE is a modifying operation that creates a new, empty data structure.

### SEARCH (data structure, key)

SEARCH is a query operation that uses a data structure and a key to return an element in the data structure or null if the element does not belong to the data structure. 


### INSERT/ADD (data structure, element)

INSERT/ADD is a modifying operaion that uses a data structure and an element to add the element to the data structure if it not does not already belong to the data structure.

### DELETE/REMOVE (data structure, element)

DELETE/REMOVE is a modifying operation that uses a data structure and an element to remove the element from the data structure if the element belongs to the data structure.

### MINIMUM/MIN (data structure)

MINIMUM/MIN is a query operation that uses a data structure to return the smallest element of the data structure.

### MAXIMUM/MAX (data structure)

MAXIMUM/MAX is a query operation that uses a data structure to return the largest element of the data structure.

### SUCCESSOR/NEXT (data structure, element)

SUCCESSOR/NEXT is a query operation that uses a data structure and an element to return the next larger element in the data structure or null if the given element is the maximum.

### PREDECESSOR/PREVIOUS (data structure, element)

PREDECESSOR/PREVIOUS is a query operation that uses a data structure and an element to return the next smaller element in the data structure or null if the given element is the minimum.

## Data Structure Examples

### Array

### Linked List

### Stack

### Queue

### Hash Map

### Tree

### Heap

### Graphs

### Object
