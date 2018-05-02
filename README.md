# ddpl_algorithm:
A simple python implementation of the DDPL algorithm 
wiki: https://en.wikipedia.org/wiki/DPLL_algorithm

#Usage:
Statements are hardcoded as they were not the primary concern of this task. 
It was built as a revision exercise for proving logical statements and learning basic use of python. 

#Implementation:
The two important functions are ddpl() and unit_prop(). The others are primarily formatting and are specific to this implementation rather than important to the algorithm.

* unit_prop() - performs the unit propagation of a given unit clause on the set of disjunctive clauses provided. 
  * first by removing clauses that contain the unit clause
    - e.g. unit clause = (u), clause = (u) | (¬v) | (w), this clause is removed 
  * secondly, by removing the negation of the unit clause from a clause
    - e.g. unit clause = (u), clause = (¬u) | (¬v) | (w), this clause becomes (¬v) | (w)
    - and (v) | (¬u) | (w) becomes (v) | (w)
    
 * ddpl() - performs the algorithm as better described on wikipedia. 
  * if the set is empty then the conjunction of disjunctive clauses must be true
  * if the empty clause is present then a contradiction has occured and therefore the premise is false. 
    - usually implying the original premise is true using proof by contradiciton
   * if a unit clause is present then propagate through the set removing it
   * if not then choose a unit clause from a disjunction of clauses and propagate with that clause.
    - first on the pressumption it is true
    - then on the presumption it is false, until it either passes or fails.
   * if the set is not empty, repeat until a truth or contradiction has been found. 

Feel free to use. 
