"use strict";

class Heap {

    constructor() {
        this.input = [7, 2, 3, 4, 9, 5, 9, -3, 72];
        this.inputRef = this.input;
        this.size = this.input.length;
        this.sizeRef = this.size;
    }
    /**
     * Get the node's index and left and right neighbour node.
     * 
     * @param {integer} i The node's index.
     * @returns {object} Node's index, left and right node.
     */
    getNodes(i) {
        let nr = 2 * i;
        let left = (nr + 1) < this.size ? nr + 1 : false;
        let right = (nr + 2) < this.size ? nr + 2 : false;
        return {
            left: left, // Left node.
            right: right, // Right node.
            main: i
        };
    }
    /**
     * Swapping nodes.
     * 
     * @param {integer} x Index of node to replace.
     * @param {integer} y Index of node to replace.
     */
    swap(x,y) {
        let first = this.input[x];
        this.input[x] = this.input[y];
        this.input[y] = first;
    }    
}
class HeapSort extends Heap {
    
    constructor() {
        super();     
    }
    /**
     * Driver method.
     */
    main() {
        this.print('Input:', this.inputRef);
        this.isMin = true; // Min heap.
        this.heapIterator();
        this.print('Min heap:', this.input);
        this.input = this.inputRef;
        this.size = this.sizeRef;
        this.isMin = false; // Max heap.
        this.heapIterator();
        this.print('Max heap:', this.input);
    }
    /**
     * 
     */
    heapIterator() {
        let j = Math.floor(this.size / 2);
        for ( j;j >= 0; j-- ) {
            this.heapify(j);
        }
        for (let j = this.size-1; j >= 0; j--) {
            this.swap(0,j);
            this.size--;
            this.heapify(0);
        }
    }
    /**
     * 
     * @param {integer} i Node's index.
     */
    heapify(i) {
      
        let nodes = this.getNodes(i);
        // If there are left nodes.
        if (nodes.left) {
            if (this.isMin && this.input[nodes.left] < this.input[i]
                || !this.isMin && this.input[nodes.left] > this.input[i]) {
                nodes.main = nodes.left;
            }
        }
        // If there are right nodes.
        if (nodes.right) {
            if (this.isMin && this.input[nodes.right] < this.input[nodes.main]
                || !this.isMin && this.input[nodes.right] > this.input[nodes.main]) {
                nodes.main = nodes.right;
            }
        }
        if (nodes.main != i) {
            this.swap(i, nodes.main);
            // Recursively call heapify.
            this.heapify(nodes.main);
        }
    }
    /**
     * Prints out the result.
     * 
     * @param {string} text 
     * @param {array} data 
     */
    print(text, data) {
        console.log(text);
        console.log(data);
    }
}

let heapSort = new HeapSort();
heapSort.main();
