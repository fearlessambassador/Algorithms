"use strict";

class Heap {
    constructor(inputArray) {
        this.input = inputArray;
        this.size = inputArray.length;
        
    }
    // Get left or right node. 1 - left, 2 -right.
    getNode(i, side) {
        return 2 * i + side; 
    }
    // Swap heap elements.
    swap(x,y) {
        var first = this.input[x];
        this.input[x] = this.input[y];
        this.input[y] = first;
    }
    
}
class HeapSort extends Heap {
    
    constructor( input ) {
        super( input );        
    }
    main() {

        this.buildMaxHeap();
        /* Move the first element to the end and the next larges telement is moved 
        to the first place every iteration. Decrease the heap size as the end of the array
        becomes ordered.*/
        for (var j = this.size-1; j >= 0; j--) {
            this.swap(0,j);
            this.size--;
            this.maxHeapify(0);
        }
        console.log(this.input);
 

    }
    buildMaxHeap() {
        /* Only half of the array needs to be iterated as checking both right and left neighbour 
        leads to check all the elements.*/
        var j = Math.floor(this.size / 2);
        for ( j;j >= 0; j-- ) {
            this.maxHeapify(j);
        }
    }
        /* Put the largest element between i, left node to i and right node to i
        to the place of i.*/
        maxHeapify(i) {

            var left = this.getNode(i, 1); // Left node.
            var right = this.getNode(i, 2); // Right node.
            var largest = i;
    
            if (left < this.size && this.input[left] > this.input[i]) {
                largest = left;
            }
    
            if (right < this.size && this.input[right] > this.input[largest]) {
                largest = right;
            }
    
            if (largest != i) {
                this.swap(i, largest);
                // we recursively call max heapify on the smallest element freshly moved so that it will moved in the array
                // regarding its size
                this.maxHeapify(largest);
            }
        }
    
        
}

var heapSort = new HeapSort([7,2,3,4,9,5]);
heapSort.main();