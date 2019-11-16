<?php
/**
 * 
 */
include_once 'class/numberGenerator.php';
class SortInitiator extends NumberGenerator
{
    public $number_set = [];
    public $length = NULL;
    public function __construct( $length )
    {
        parent::__construct( $length );       
        $this->number_set = $this->result;
        $this->length = $length;
    }
    public function heap()
    {
        include_once 'class/Heap_.php';
        $heap_sort = new Heap( $this->length, $this->number_set );
        $heap_sort->create_heap();
        $result = $heap_sort->heap;
        print_r($this->number_set);
        echo '<br>';
        $heap_sort->sort();
        //return $result;

    }
    
}
$test = new SortInitiator(10);
print_r( $test->heap() );