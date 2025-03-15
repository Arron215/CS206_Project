***CS206 Project - Group Arron and Loi***  
# Exploring the Impact of Randomized Splitting Strategies on Delta Debugging

This repo contains the prototype that were created for the project. The sanitize.py script is the toy function and includes a generated test input set. 

The specific ddmin algorithms are split into different scripts to allow for easier testing. 

To run the experiment, use the command
  ```bash
  python3 test_sanitize.py
  ```
The prototypes developed were based on the original ddmin algorithm detailed by Zeller in The Debugging Book website. Our implementations focus on the testing of random sets instead of the initial predetermined split of the input set until a set point. We have 2 control groups, ddmin and ddmin\_random. The ddmin algorithm is a copy of the one referenced in the website. Other implementations were available, but it felt correct to borrow the implementation created by the original author of ddmin. 

*ddmin\_random* is implemented based on RS-DD algorithm and can serve as a control to measure the effect of unmitigated randomness in a dataset. This algorithm will continue input testing with a random splitting of the input set and reduces the failure-inducing set the same way traditional DD will. 

*ddmin\_hybrid* is the implementation that utilizes the approach that we have outlined in Hybrid-DD. First, the ddmin algorithm will select a random point along the input to split into parts. The potential inputs will then be inputted into the test function and the ddmin algorithm will reduce as normal. On the next iteration, ddmin\_hybrid will either revert back to traditional ddmin or continue selecting random split points depending on if the input is less than half of the original input. If the input is less than half of its original size, then we revert to traditional ddmin. Not much experimentation was done on when to revert, as the point to revert would depend on the kind of failure-inducing test input. 

*ddmin\_alt* is the implementation that utilizes the approach outlined in RS-TDD. The implementation is similar to ddmin\_hybrid, but instead of splitting after the input set is half of its original size, the algorithm will test a randomly generated input and its complement. If the complement and the randomly generated input return a PASS and a FAIL, then the algorithm will continue testing with the failing input. Otherwise, the algorithm will continue with selecting a random subset of the current input. In the event that the algorithm attempts \textit{n} tests, where n is the size of the input, then the algorithm determines that there are no further possible splits and reverts back to traditional DD.

