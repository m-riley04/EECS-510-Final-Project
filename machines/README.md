# Machines
For our program, NFAs are parsed from a text file. This allows for generalization and very easy modification.

## Format
The format of each "machine" file is as follows:
```
[state_0] [state_1] [state_n]
[symbol_0] [symbol_1] [symbol_n]
[start_state]
[accept_state_0] [accept_state_1] [accept_state_n]
[from_state_0] [transition_symbol_0] [to_state_0]
[from_state_1] [transition_symbol_1] [to_state_1]
[from_state_n] [transition_symbol_n] [to_state_n]
```

### Line 1: States 
a space-separated list of states

Example:
```
q0 q1 q2
```

### Line 2: Symbols
a space-separated list of symbols

> NOTE: Lambda (~) does not *need* to be specified, but can be.

Example:
```
A B C D E F G
```

### Line 3: Start State
a singular start state

Example:
```
q0
```

### Line 4: Accept States
a space-separated list of accept states

Example:
```
q0 q2
```

### Line 5+: Transitions
a space-separated list of 3 components:
- From State: the outbound state of the transition
- Symbol: the symbol to transition on
- To State: the inbound state of the transition

Example:
```
q0 A q1
q0 A q2
q0 B q0
q2 D q1
```