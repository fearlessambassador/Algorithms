<?php


class NumberGenerator
{

    public $length = NULL;
    public $result = [];
    private $count = NULL;

    public function __construct( $length )
    {      
        $this->length = $length; 
        $this->count = 0;
        $this->generate();
    }
    public function generate()
    {
        if( $this->count === $this->length )
        {
            return;
        }
        $number = $this->get_random_number();        
        $this->result[ $this->count ] = $number;
        $this->increase();
        $this->generate();
    }
    private function get_random_number()
    {
        return rand( 1, 500 );
    }
    private function increase()
    {
        $this->count++;
    }
}