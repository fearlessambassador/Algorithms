<?php
/**
 * 
 */

 class Heap {

    public $heap = NULL;
    public $size = NULL;
    /**
     * 
     */
    public function __construct($input=[]) {
        $this->heap = $input;
        $this->size = count($input);
    }
 }
 class HeapSort {

    private $heap = NULL;
    /**
     * 
     */
    public function __construct(Heap $heap) {
        $this->heap = $heap;
        $this->buildMaxHeap();
        for($i=$this->heap->size-1;$i>=0;$i--) {
            $this->swapNode(0, $i);
            $this->heap->size--;
            $this->maxHeapify(0);
        }
        print_r($this->heap->heap);
    }
    private function buildMaxHeap() {

        $i = (int)$this->heap->size / 2;
        for($i; $i>=0; $i--) {
            $this->maxHeapify($i);
        }
        
    }
    private function maxHeapify($index) {
        $leftNode = $this->getNode($index, 1);
        $rightNode = $this->getNode($index, 2);
        $largestNode = $index;
        $size = $this->heap->size;
        if($leftNode < $size && $this->heap->heap[$leftNode] > $this->heap->heap[$index]) {
            $largestNode = $leftNode;
        }
        if($rightNode < $size && $this->heap->heap[$rightNode] > $this->heap->heap[$largestNode]) {
            $largestNode = $rightNode;
        }
        if($largestNode != $index) {
            $this->swapNode($index, $largestNode);
            $this->maxHeapify($largestNode);
        }
    }
    private function swapNode($x, $y) {
        $firstNode = $this->heap->heap[$x];
        $this->heap->heap[$x] = $this->heap->heap[$y];
        $this->heap->heap[$y] = $firstNode;
    }
    private function getNode($index, $side) {
        return 2 * $index + $side; 
    }
 }
 $heap = new Heap([1,9,4,5,6,3]);
 $heapSort = new HeapSort($heap);
