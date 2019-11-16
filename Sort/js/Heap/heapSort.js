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
    //
    swap(x,y) {
        var first = this.input[x];
        this.input[x] = this.input[y];
        this.input[y] = first;
    }
    
}
class HeapSort extends Heap{
    
    constructor( input ) {
        super( input );        
    }
    main() {

        this.buildMaxHeap();

        // the first element is moved to the end and the next largest element is moved to the first place on each iteration
        // the heapsize decreases because the end of the array become ordered
        for (var j = this.size-1; j >= 0; j--) {
            //this.input.swap(0, j);
            this.swap(0,j);
            this.size--;
            this.maxHeapify(0);
        }
        console.log(this.input);
 

    }
    buildMaxHeap() {
        // we only need to process the first half of the array because all 
        // element will be checked (as we check the
        // right and left node)
        var j = Math.floor(this.size / 2);
        for ( j;j >= 0; j-- ) {
            this.maxHeapify(j);
        }
    }
        // the largest element between i, left(i) and right(i) will take the place of i
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
                //this.input.swap(i, largest);
                this.swap(i, largest);
                // we recursively call max heapify on the smallest element freshly moved so that it will moved in the array
                // regarding its size
                this.maxHeapify(largest);
            }
        }
    
        
}

var heapSort = new HeapSort([1,2,3,4, 9, 5]);
heapSort.main();