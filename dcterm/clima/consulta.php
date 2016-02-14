<?php

if (isset($_GET['dato'])) {
    $par = $_GET['dato'];
    if ($par == 'temp') {
        $line = '';
        $f = fopen("clima.txt", 'r');

        $line = fgets($f);

        echo $line;
        fclose($f);
    }
}
?>


