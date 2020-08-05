'use strict';
class MergeSort {

    constructor() {
        this.input = [340, 1, 22, 3, 76, 23, 4];
        this.middle = 0;   
    }
    setMiddle(length) {
        this.middle = Math.floor(length / 2);        
    }
    merge(left, right) {
        let resultArray = [], leftIndex = 0, rightIndex = 0;
    // Insert values to the sorted array.
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        resultArray.push(left[leftIndex]);
        leftIndex++; // move left array index.
      } else {
        resultArray.push(right[rightIndex]);
        rightIndex++; // move right array index.
      }
    }
    
    // Concat the array into two slices.
    return resultArray
    .concat(left.slice(leftIndex))
    .concat(right.slice(rightIndex));
    }
    mergeSort(unsortedArray) {

        if (unsortedArray.length <= 1) {
            return unsortedArray;
        }
        
        this.setMiddle(unsortedArray.length);

        // This is where we will be dividing the array into left and right
        const left = unsortedArray.slice(0, this.middle);
        const right = unsortedArray.slice(this.middle);
        let result = this.merge(
            this.mergeSort(left), this.mergeSort(right)
        );
        return result;
    }
}

var mSort = new MergeSort();
var result = mSort.mergeSort(mSort.input)
console.log(result);