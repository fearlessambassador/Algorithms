<?php
/**
 * 
 */
/* class HeapSort extends Heap
{

} */
/**
 * 
 */
class Heap extends Node
{
  
  private $count = NULL;
  private $length = NULL;
  public $heap = NULL;
  private $number_set = NULL;
  private $current_size = NULL;
  public function __construct( $length, &$number_set )
  {
    $this->count = 0;
    $this->length = $length;
    $this->number_set = $number_set;
    $this->current_size = 0;
    
  }

  public function create_heap()
  {
    if( $this->count === $this->length )
    {
     // prin_r($this->heap );
      return;
    }
    $key = $this->count;
    $value = $this->number_set[ $key ];
    $Node = new Node( $value );
    
    $this->_current_Size = 0;
    $this->insert( $key, $Node );
    $this->current_size++;
    $this->count++;
    $this->create_heap();

  }
  private function insert( $key, Node $value )
  {
    
    $this->heap[ $key ] = $value;
    
  }
  private function get_size()
  {
    
    return $this->current_size;
  }
  private function heapify(Int $i = null)
  {
    $larger_Child = null;
    $top = $this->heap[$i];
    $x = (int)( $this->current_size /2 );
    while ($i < $x) { // not on bottom row
      $leftChild = 2 * $i + 1;
      $rightChild = $leftChild + 1;
      
    // find larger child
    if ($rightChild < $this->current_size 
    && $this->heap[$leftChild] < $this->heap[$rightChild]) // right child exists?
    {
      
    $larger_Child = $rightChild;
    } else {
    
    $larger_Child = $leftChild;
    }
    
    if ($top->getKey() >= $this->heap[$larger_Child]->getKey()) {
      break;
      }
      
      // shift child up
      $this->heap[$i] = $this->heap[$larger_Child]; 
      $i = $larger_Child; // go down
      }
      echo $top->getKey() . '.... ' . $i;
      echo '<br>';
      for($j=0;$j<$this->length; $j++)
      {
        echo '__ ';
        echo $this->heap[$j]->getKey();
      }
      echo '<br>'; 
      $this->heap[$i] = $top; // root to index
    
  }
  public function remove()
  {
      $root = $this->heap[0];
      // put last element into root
      $this->current_size--;
      $this->heap[0] = $this->heap[$this->current_size];
      
      $this->heapify(0); 
      return $root; 
  }
  public function sort()
  {
    $size = $this->get_size();
    $size = (int)( $size /2 ) - 1;
    
    for( $i = $size; $i >= 0; $i-- )
    {
      $this->heapify( $i);
    }
    
    for ($j = $size - 1; $j >= 0; $j--) { 
      $BiggestNode = $this->remove();
      
      // use same nodes array for sorted elements
      $this->insert($j, $BiggestNode);
      
      } 
      
    print_r( $this->heap );

  }
  public function asArray()
{
$arr = array();
for ($j = 0; $j < sizeof($this->heap); $j++) {
$arr[] = $this->heap[$j]->getKey();
}

return $arr;
}
  
}

/**
 * 
 */
class Node
{
  private $_i; 

  public function __construct($key)
  {
      $this->_i = $key;
  }

  public function getKey()
  {
      return $this->_i;
  }
}