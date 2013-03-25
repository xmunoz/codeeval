<?php

ini_set('auto_detect_line_endings',true);

/**
 * Reads in data from file and stores each line in an array
 * @file_name - the file name as a string
 *
 */

function read_in_data($file_name) {
  $data = array();
  $file_handle = fopen($file_name, "r");
  
  while(!feof($file_handle)) {
    $line = fgets($file_handle);
    $data[] = $line;
  }

  fclose($file_handle);
  return $data;
}


/**
 * Preforms the fizzbuzz operation on a string
 * @string - a space delimited string of values
 */

function fizzbuzz($string) {
  $elems = explode(' ', $string);
  $i = 1;
  $output = array();
  while ($i <= end($elems)) {
    $output[$i] = '';
    if ($i%$elems[0] == 0){
      $output[$i] = 'F';
    }
    if ($i%$elems[1] == 0) {
      $output[$i] .= 'B';
    }
    if ($output[$i] == '') {
      $output[$i] = $i;
    }
    ++$i;
  }
  return implode(' ', $output);
}

/**
 * Main function
 *
 */

function main_f() {
  $args = $_SERVER['argv'];
  
  if (count($args) != 2) {
    return "Wrong number of args passed to script
    Example usage: php fizzbuzz.php test_file\n";
  }

  $data = read_in_data($args[1]);

  $output = array();
  
  foreach ($data as $set) {
    if ($set) {
      $output[] = fizzbuzz($set);
    }
  }
  
  foreach ($output as $string) {
    print $string . "\n";    
  }

}

main_f();


?>
