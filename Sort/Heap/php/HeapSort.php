<?php
/**
 * Max heap sort in php.
 */

 /**
  * Heap.
  */
 class Heap {

    public $heap = NULL;
    public $size = NULL;
    /**
     * Creating a heap object.
     * @param array $input the array to be sorted.
     */
    public function __construct(array $input=[]) {
        $this->heap = $input;
        $this->size = count($input);
    }
 }
 /**
  * HeapSort.
  * Sorts the input array with the max heap algorithm.
  * @return array the sorted array.
  */
 class HeapSort {

    private $heap = NULL;
    /**
     * Constructor.
     * @param Heap $heap {int size, array heap}.
     * @return array the sorted array.
     */
    public function __construct(Heap $heap) {
        // Create a local heap.
        $this->heap = $heap;
        $this->buildMaxHeap();
        for($i=$this->heap->size-1;$i>=0;$i--) {
            // Replace the first node with node[$i].
            $this->swapNode(0, $i);
            // Reduce the heap size by one.
            $this->heap->size--;

            $this->maxHeapify(0);
        }
        return $this->heap->heap;
    }
    /**
     * Build max heap.
     */
    private function buildMaxHeap() {
        // Only the half of the input array need to be iterated.
        $i = (int)$this->heap->size / 2;
        for($i; $i>=0; $i--) {
            $this->maxHeapify($i);
        }
        
    }
    /**
     * Put the largest element between $index, left and right 
     * neighbour to the place of the $index.
     * @param integer $index index of the heap.
     */
    private function maxHeapify(int $index) {
        // Get neighbour nodes.
        $leftNode = $this->getNode($index, 1);
        $rightNode = $this->getNode($index, 2);
        // Get middle node.
        $largestNode = $index;
        $size = $this->heap->size;
        // If left node is larger.
        if($leftNode < $size && 
        $this->heap->heap[$leftNode] > $this->heap->heap[$index]) {
            $largestNode = $leftNode;
        }
        // If right node is larger.
        if($rightNode < $size && 
        $this->heap->heap[$rightNode] > $this->heap->heap[$largestNode]) {
            $largestNode = $rightNode;
        }
        // If largest is not the middle node, replace.
        if($largestNode != $index) {
            $this->swapNode($index, $largestNode);
            $this->maxHeapify($largestNode);
        }
    }
    /**
     * Replace the two nodes with each other.
     * @param integer $x node to replace.
     * @param integer $y node to replace.
     */
    private function swapNode(int $x, int $y) {
        $firstNode = $this->heap->heap[$x];
        $this->heap->heap[$x] = $this->heap->heap[$y];
        $this->heap->heap[$y] = $firstNode;
    }
    /**
     * Get the desired node.
     * @param integer $index index of the node.
     * @param integer $side the requested neighbour node of $index, 
     * 1 - left, 2 - right.
     * @return integer index of the node.
     */
    private function getNode(int $index, int $side) {
        return 2 * $index + $side; 
    }
 }

 $heap = new Heap([1,9,4,5,6,3]);
 $heapSort = new HeapSort($heap);
print_r($heapSort);