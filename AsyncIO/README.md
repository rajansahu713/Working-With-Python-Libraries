<h1 align="center"> Here we going to discuss every concept which are related to Python asyncio</h1>

## Sub-routine
* A subroutine and a function are essentially the same thing, with one difference: A function returns some sort of value (usually via the stack or CPU register), while a subroutine does not. Whether subroutine or function, it is a block of executable code, having exactly one point of entry. 


## Co-routine:
* A co-routine is also a block of executable code, and, just like a subroutine, it has one point of entry. However, it also has one or more points of re-entry. More on this later. 
* it has one or more points of re-entry. A point of re-entry means that the co-routine can allow for some other block of code outside of itself to have some execution time, and then at some future time have execution time resume back within its own block of code. This implies that the parameters and automatic variables of the co-routine are preserved (and restored if need be) whenever execution is yielded to an external block of code and then returns to that of the co-routine. A co-routine is something that is not directly implemented in every programming language, although it is common to many assembly languages. 


## It seems to me there are two principal motivations in implementing a co-routine design pattern:  
* Overcoming the limitations of a single-threaded process; 
* And  hoping to achieve better computational performance. 

## Motivation
* is clear to understand when the process must address many things at once where a single thread is a must. 



### Differences co-routine and sub-routine:
1. Co-routine doesn't have a master-slave relationship while subroutine has. 
2. A subroutine has a single entry point, while co-routine may have a entry and multiple re-entry points.
3. The calling program is suspended during execution of the called subroutine. Co-routines provide quasi-concurrent execution. 

### Similarities: 
1. Both co-routines and subroutines are able to use return. 
2. The execution of both co-routines and subroutines are not overlapped.


## Reference 
* http://en.wikipedia.org/wiki/Coroutine.