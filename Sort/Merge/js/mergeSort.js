'use strict';
class MergeSort {

    constructor() {
        this.input = [340, 1, 22, 3, 76, 23, 4];
        console.log(this.input)
        this.middle = 0;
        

    }
    setMiddle(length) {
        this.middle = Math.floor(length / 2);
        
    }
    merge(left, right) {
        let resultArray = [], leftIndex = 0, rightIndex = 0;
    // We will concatenate values into the resultArray in order
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        resultArray.push(left[leftIndex]);
        leftIndex++; // move left array cursor
      } else {
        resultArray.push(right[rightIndex]);
        rightIndex++; // move right array cursor
      }
    }
    
    // We need to concat here because there will be one element remaining
    // from either left OR the right
    //console.log(flag)
    return resultArray
    .concat(left.slice(leftIndex))
    .concat(right.slice(rightIndex));
    }
    mergeSort(unsortedArray) {
        console.log(unsortedArray);
        if (unsortedArray.length <= 1) {
            return unsortedArray;
        }
        // In order to divide the array in half, we need to figure out the middle
        this.setMiddle(unsortedArray.length);
        //console.log(unsortedArray);
        // This is where we will be dividing the array into left and right
        const left = unsortedArray.slice(0, this.middle);
        const right = unsortedArray.slice(this.middle);
        let test = this.merge(
            this.mergeSort(left), this.mergeSort(right)
        );
        //console.log(right)
        return test;
    }
}



  
  
  var mergeSort1 = new MergeSort();
  //console.log(mergeSort1['input'])
  console.log(mergeSort1.mergeSort(mergeSort1.input));













  // Merge the two arrays: left and right
/* function merge1 (left, right) {
    let resultArray = [], leftIndex = 0, rightIndex = 0;
  
    // We will concatenate values into the resultArray in order
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        resultArray.push(left[leftIndex]);
        leftIndex++; // move left array cursor
      } else {
        resultArray.push(right[rightIndex]);
        rightIndex++; // move right array cursor
      }
    }
  
    // We need to concat here because there will be one element remaining
    // from either left OR the right
    //console.log(flag)
    let test = resultArray
    .concat(left.slice(leftIndex))
    .concat(right.slice(rightIndex));
    //console.log(test)
    return test;
  } */
/* // Merge Sort Implentation (Recursion)
function mergeSort (unsortedArray) {
    console.log(unsortedArray);
    // No need to sort the array if the array only has one element or empty
    if (unsortedArray.length <= 1) {
      return unsortedArray;
    }
    // In order to divide the array in half, we need to figure out the middle
    const middle = Math.floor(unsortedArray.length / 2);
    //console.log(unsortedArr);
    // This is where we will be dividing the array into left and right
    const left = unsortedArray.slice(0, middle);
    const right = unsortedArray.slice(middle);
    
    // Using recursion to combine the left and right
    let test1 = mergeSort(left);
    let test2 = mergeSort(right);
    let test5 = new MergeSort();
    let test4 =  test5.merge(
        test1, test2
      );
      //console.log(unsortedArr)
      //console.log(test2)
    return test4;
  } */