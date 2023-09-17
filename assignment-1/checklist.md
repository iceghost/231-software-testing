# Checklist

## I - DEVIATION OBJECTIVE

### I.1 - Deviation

|    |                                                                                           |
|:--:|-------------------------------------------------------------------------------------------|
|  1 |  Does the code correctly implement the   design?                                          |
|  2 |  Does the code implement   more than the design?                                          |
|  3 |  Is every parameter of   every method passing mechanism (value or reference) appropriate? |
|  4 |  Does every method   return the correct value at every method return point?               |

## II - OMISSION OBJECTIVE

### II.1 - Omission

|    |                                                   |
|:--:|---------------------------------------------------|
| 5  |  Does the code completely implement the   design? |

## III - DEFECT OBJECTIVE

### III.1 – Variable and Constant Declaration

|    |                                                                                        |
|:--:|----------------------------------------------------------------------------------------|
| 6  |  Are descriptive variable and constant names   used in accord with naming conventions? |
| 7  |  Is every variable   correctly typed?                                                  |
| 8  |  Is every variable   properly initialized?                                             |
| 9  |  Are all for-loop   control variables declared in the loop header?                     |
| 10 |  Are there variables   that should be constants?                                       |
| 11 |  Are there attributes   that should be local variables?                                |
| 12 |  Do all attributes have   appropriate access modifiers (private, protected, public)?   |

### III.2 – Method Definition

|    |                                                                                   |
|:--:|-----------------------------------------------------------------------------------|
| 13 |  Are descriptive method names used in accord   with naming conventions?           |
| 14 |  Do all methods have   appropriate access modifiers (private, protected, public)? |
| 15 |  Is every method   parameter value checked before being used?                     |

### III.3 – Class Definition

|    |                                                                            |
|:--:|----------------------------------------------------------------------------|
| 16 |  Does each class have an appropriate   constructor?                        |
| 17 |  Do any subclasses have   common members that should be in the superclass? |

### III.4 – Data Reference

|    |                                                                                  |
|:--:|----------------------------------------------------------------------------------|
| 18 |  For every array reference: Is each subscript   value within the defined bounds? |
| 19 |  For every object or   array reference: Is the value certain to be non-null?     |

### III.5 – Computation/Numeric

|    |                                                            |
|:--:|------------------------------------------------------------|
| 20 |  Are there any computations with mixed data   types?       |
| 21 |  Is overflow or   underflow possible during a computation? |
| 22 |  Are parentheses used to   avoid ambiguity?                |
| 23 |  Are divisors tested for   zero or noise?                  |

### III.6 – Comparison/Relational

|    |                                                                                     |
|:--:|-------------------------------------------------------------------------------------|
| 24 |  For every boolean test: Is the correct   condition checked?                        |
| 25 |  Are the comparison   operators correct?                                            |
| 26 |  Is each boolean   expression correct?                                              |
| 27 |  Are there improper and   unnoticed side-effects of a comparison?                   |
| 28 |  Has an   "&" inadvertently been interchanged with a   "&&" or a "\|" for a "\|\|"? |
| 29 |  Is every three-way   branch (less,equal,greater) covered?                          |

### III.7 – Control Flow

|    |                                                                                            |
|:--:|--------------------------------------------------------------------------------------------|
| 30 |  Will all loops terminate?                                                                 |
| 31 |  When there are multiple   exits from a loop, is each exit necessary and handled properly? |
| 32 |  Does each switch   statement have a default case?                                         |
| 33 |  Are missing switch case   break statements correct and marked with a comment?             |
| 34 |  Can any nested if   statements be converted into a switch statement?                      |
| 35 |  Are null bodied control   structures correct and marked with braces or comments?          |
| 36 |  Does every method   terminate?                                                            |
| 37 |  Are all exceptions   handled appropriately?                                               |
| 38 |  Do named break   statements send control to the right place?                              |

### III.8 – Input/Output

|    |                                                                      |
|:--:|----------------------------------------------------------------------|
| 39 |  Have all files been opened before use?                              |
| 40 |  Have all files been   closed after use?                             |
| 41 |  Is buffered data   flushed?                                         |
| 42 |  Are files checked for   existence before attempting to access them? |

### III.9 – Module Interface

|    |                                                                                                                                     |
|:--:|-------------------------------------------------------------------------------------------------------------------------------------|
| 43 |  Are the number, order, types, and values of   parameters in every method call in agreement with the called method's   declaration? |
| 44 |  Do the values in units   agree (e.g., inches versus yards)?                                                                        |

### III.10 – Comment

|    |                                                                                                           |
|:--:|-----------------------------------------------------------------------------------------------------------|
| 45 |  Does every method, class, and file have an   appropriate header comment?                                 |
| 46 |  Does every   attribute,variable or constant declaration have a comment?                                  |
| 47 |  Is the underlying   behavior of each method and class expressed in plain language?                       |
| 48 |  Is the header comment   for each method and class consistent with the behavior of the method or   class? |
| 49 |  Are all comments   consistent with the code?                                                             |
| 50 |  Do the comments help in   understanding the code?                                                        |
| 51 |  Are there enough   comments in the code?                                                                 |
| 52 |  Are there too many   comments in the code?                                                               |

### III.11 – Layout and Packing

|    |                                                                   |
|:--:|-------------------------------------------------------------------|
| 53 |  Is a standard indentation and layout format   used consistently? |
| 54 | For each method: Is it no more than about 60 lines long?          |

### III.12 – Storage Usage

|    |                           |
|:--:|---------------------------|
| 55 |  Are arrays large enough? |

### III.13 – Performance

|    |                                                                                                 |
|:--:|-------------------------------------------------------------------------------------------------|
| 56 |  Can the cost of recomputing a value be   reduced by computing it once and storing the results? |
| 57 |  Is every result that is   computed and stored actually used?                                   |
| 58 |  Can a computation be   moved outside a loop?                                                   |
| 59 |  Are there tests within   a loop that do not need to be done?                                   |

## V - AMBIGUITY OBJECTIVE

### V.1 – Variable and Constant Declaration

|    |                                                                                     |
|:--:|-------------------------------------------------------------------------------------|
| 60 |  Are there variables with confusingly similar   names?                              |
| 61 |  Are all variables   properly defined with meaningful, consistent, and clear names? |

## VI - REDUNDANCE OBJECTIVE

### VI.1 – Variables

|    |                                                               |
|:--:|---------------------------------------------------------------|
| 62 |  Are there any redundant or unused variables   or attributes? |
| 63 |  Could any non-local   variables be made local?               |

### VI.2 – Method Definition

|    |                                              |
|:--:|----------------------------------------------|
| 64 |  Are there any uncalled or unneeded methods? |

### VI.3 – Performance

|    |                                                                                        |
|:--:|----------------------------------------------------------------------------------------|
| 65 |  Can any code be replaced by calls to   external reusable objects?                     |
| 66 |  Are there any blocks of   repeated code that could be condensed into a single method? |
