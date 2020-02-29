/**
 * Insertion sort algorith in Javascript.
 * Sorts the array in ascending order, 
 * then sorts the sorted array again in descending order recursively.
 * Prints out the original array and the two sorted arrays.
 */

var set = [11, 3, 5, 8, -3, 4, -9, 0];
// Print the original array.
console.log(set);

var sortedSet = insertionSort(set);
// Print the sorted array (ascending).
console.log(sortedSet);

var sortedSetRecursive = insertionSortRecursive(sortedSet, sortedSet.length);
// Print the sorted array (descending).
console.log(sortedSetRecursive);

function insertionSort(set)
{
    for (let i = 1; i < set.length; i++) {

        let elem = set[i];
        if (elem < set[0]) {
            set.unshift(set.splice(i, 1)[0]);
        } else if (elem > set[i - 1]) {
            continue;
        } else {
            for (let j = 1; j < i; j++) {

                if (elem > set[j - 1] && elem < set[j]) {
                    set.splice(j, 0, set.splice(i, 1)[0]);
                }
            }
        }
    }
    return set;
}

function insertionSortRecursive(set, length)
{
    if (length <= 1) {
        return set;
    }
    
    let lastElem = set[length - 1];
    let j = length - 2;
    while (j >= 0 && set[j] < lastElem) {
        set[j + 1] = set[j];
        j--;
    }
    set[j] = lastElem;
    insertionSortRecursive(set, length - 1);
}