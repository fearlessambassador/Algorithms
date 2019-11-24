"use strict";

class Heap {
    constructor(inputArray) {
        this.input = inputArray;
        this.maxSize = inputArray.length;
        this.minSize = inputArray.length;
        this.maxHeapResult = this.input;
        this.minHeapResult = this.input;
        console.log('Input:');
        console.log(this.input);
    }
    // Get left or right node. 1 - left, 2 -right.
    getNode(i, side) {
        return 2 * i + side; 
    }
    // Swap heap elements.
    swap(x,y, input) {
        var first = input[x];
        input[x] = input[y];
        input[y] = first;
        return input;
    }
    
}
class HeapSort extends Heap {
    
    constructor( input ) {
        super( input );     
    }
    main() {
        this.maxHeap();
        this.minHeap();
 

    }
    minHeap() {
        this.buildMinHeap();
        for (var j = this.minSize-1; j >= 0; j--) {
            this.maxHeapResult = this.swap(0,j, this.minHeapResult);
            this.minSize--;
            this.minHeapify(0);
        }
        console.log('Min heap:');
        console.log(this.minHeapResult);
    }
    maxHeap() {
        this.buildMaxHeap();
        /* Move the first element to the end and the next largest element is moved 
        to the first place every iteration. Decrease the heap size as the end of the array
        becomes ordered.*/
        for (var j = this.maxSize-1; j >= 0; j--) {
            this.maxHeapResult = this.swap(0,j, this.maxHeapResult);
            this.maxSize--;
            this.maxHeapify(0);
        }
        console.log('Max heap:');
        console.log(this.maxHeapResult);
    }
    buildMinHeap() {
        var j = Math.floor(this.minSize / 2);
        for ( j;j >= 0; j-- ) {
            this.minHeapify(j);
        }
     
    }
    minHeapify(i) {
        var left = this.getNode(i, 1); // Left node.
        var right = this.getNode(i, 2); // Right node.
        var smallest = i;
    
        if (left < this.minSize && this.minHeapResult[left] < this.minHeapResult[i]) {
            smallest = left;
        }
    
        if (right < this.minSize && this.minHeapResult[right] < this.minHeapResult[smallest]) {
            smallest = right;
        }
    //console.log(smallest)
        if (smallest != i) {
            this.minHeapResult = this.swap(i, smallest, this.minHeapResult);
            // we recursively call max heapify on the smallest element freshly moved so that it will moved in the array
            // regarding its size
            this.minHeapify(smallest);
        }
    }
    buildMaxHeap() {
        
        /* Only half of the array needs to be iterated as checking both right and left neighbour 
        leads to check all the elements.*/
        var j = Math.floor(this.maxSize / 2);
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
    
            if (left < this.maxSize && this.maxHeapResult[left] > this.maxHeapResult[i]) {
                largest = left;
            }
    
            if (right < this.maxSize && this.maxHeapResult[right] > this.maxHeapResult[largest]) {
                largest = right;
            }
    
            if (largest != i) {
                this.maxHeapResult = this.swap(i, largest, this.maxHeapResult);
                // we recursively call max heapify on the smallest element freshly moved so that it will moved in the array
                // regarding its size
                this.maxHeapify(largest);
            }
        }
    
        
}

var heapSort = new HeapSort([7,2,3,4,9,5]);
heapSort.main();