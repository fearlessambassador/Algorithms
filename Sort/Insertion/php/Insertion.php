<?php
/**
 * Insertion sort algorith in Php.
 * Sorts the array in ascending order, 
 * then sorts the sorted array again in descening order recursively.
 * Prints out the original array and the two sorted arrays.
 */

$set = [11, 3, 5, 8, -3, 4, -9, 0];
$length = count($set);
// Print the original array.
print_r($set);

InsertionSort($set, $length);
// Print the sorted array (ascending).
print_r($set);

InsertionSortRecursive($set, $length);
// Print the sorted array (descending).
print_r($set);

 /**
  * Insertion sort algorithm (ascending).
  * @param set {array[int]} the array to sort.
  * @param length {int} the length of the array.
  */
 function InsertionSort(&$set, $length)
 {
     // Start from second element, as the first 
     // is already sorted.
     for ($i=1; $i<$length; $i++) {
         $elem = $set[$i];
         $j = $i;

         // Shift elems if the previous elem is bigger.
         while ($j>0 && $set[$j-1] > $elem) {
             $set[$j] = $set[$j-1];
             $j--;
         }
         $set[$j] = $elem;
     }
 }
 /**
  * Insertion sort algorithm (descending, recursive).
  * @param set {array[int]} the array to sort.
  * @param length {int} the length of the array.
  * return void.
  */
 function InsertionSortRecursive(&$set, $length)
 {
    // Return at the end.
    if ($length <= 1)
    {
        return;
    }
    // Sort first n-1 elements 
    InsertionSortRecursive($set, $length - 1);

    // Insert last element at its correct  
    // position in sorted array.
    $last = $set[$length - 1];
    $j = $length - 2;

    // Move elements of arr[0..i-1], that are 
    // greater than key, to one position ahead 
    // of their current position.
    while ($j >= 0 && $set[$j] < $last)
    {
        $set[$j + 1] = $set[$j];
        $j--;
    }
    $set[$j + 1] = $last;    
 }