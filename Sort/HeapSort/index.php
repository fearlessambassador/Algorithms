<?php
/**
 * 
 */
include_once 'class/node.php';
class Heap extends Node
{
  
  private $count = NULL;
  private $length = NULL;
  public $heap = NULL;
  private $number_set = NULL;
  private $current_size = NULL;
  public function __construct( $length, $number_set )
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
    $this->insert( $key, $value );
    $this->count++;
    $this->create_heap();

  }
  private function insert( $key, $value )
  {
    $this->heap[ $key ] = $value;
  }
  
} 




















/*   include_once 'class/node.php';
  include_once 'class/heap.php';
  include_once 'class/numberGenerator.php';
  $test = new NumberGenerator( 7 );
  $arr = $test->result;
  echo "Original Array : ";
  echo implode(', ',$arr )."<br>"; 
  $Heap = new Heap();
  foreach ($arr as $key => $val) {
  $Node = new Node($val);
  $Heap->insertAt($key, $Node);
  $Heap->incrementSize();
  }
  print_r( $Heap->heap_Array );
  $result = heapsort($Heap);
  echo "\nSorted Array : ";
  echo implode(', ',$result)."<br>";  */ 


  ?>