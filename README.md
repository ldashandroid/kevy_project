kevy_project
============

You are given a Secret which encapsulates a function that accepts a single integer parameter and returns an integer. In Java or a language of your choice, write an application that determines if Secret is an additive function secret(x+y) = secret(x) + secret(y) for all prime numbers less than N where N is a given integer.  Assume you are going to ship this code. Use your judgement to determine what you need to include. Document any assumptions or choices you make in your implementation. Also, include an explanation of your choice of language .


My Choices
I chose Python due to it already having a standard unittest library built in. It's also the language I'm most familiar. I assumed that this application would be better as a library method figuring that the secret and the n(the number that all prime numbers have to be less than) would be passed as parameters.  I assumed the secret would a python function. Since this code should be shippable Unit Tests for all the functions have been provided. 
