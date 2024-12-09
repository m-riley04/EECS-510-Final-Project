# Testing
This folder contains text files for the NFA that are used for testing. 

## Acceptance Tests
Acceptance tests are for testing to see if the given input string correctly displays "accept" or "reject". The format for `acceptance_tests.txt` is as follows:

```
[input string]:[expected outcome] 
```

where "input string" is the input to test against the machine, and "expected outcome" is the expected outcome represented as a single character ('a' for "accept" or 'r' for "reject").