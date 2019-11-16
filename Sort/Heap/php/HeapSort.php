<?php
/**
 * 
 */
echo 'eee';
 class Heap {

    public $heap = NULL;
    public $size = NULL;
    /**
     * 
     */
    public function __construct($input=[]) {
        self::$heap = $input;
        self::$size = count($input);
    }
 }
 class HeapSort {

     /**
      * 
      */
      public function __construct(Heap $heap) {
        print_r($heap);
    }
 }
 $heap = new Heap([1,4,5,6,3]);
 $heapSort = new HeapSort($heap);
