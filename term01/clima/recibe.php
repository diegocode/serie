<?php
if (isset($_GET['datos'])) {
    $par = $_GET['datos'];

    $f = fopen("clima.txt", 'w');
    fwrite($f, $par);
    fclose($f);
}
?>