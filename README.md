# Introduction-to-Sets
One of HakerRank problem

## To Do
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Where,    average = (Sum of Distinct Heights) / (Total Number of Distinct Heights)

Complete the average function in the editor below.

Returns float : the resulting float value rounded to 3 places after the decimal

## Solution 
- First convert the array into set by which all the duplicate elements are removed
- Then use "sum()" function which gives sum of all elements of the set.
- Now for getting average, divide the Sum of Distinct Heights by length of the set.
- Return the average Value.
