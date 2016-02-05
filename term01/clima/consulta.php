<?php

if (isset($_GET['dato'])) {
    $par = $_GET['dato'];
    if ($par == 'seg')
        echo date("s");
    else
    if ($par == 'temp') {
        //$fh = fopen("/home/diegocode/Documents/src/serie/term01/clima.txt", 'r');

        $line = '';

        $f = fopen("clima.txt", 'r');


        $line = fgets($f);
//$f = fopen("/home/diegocode/Documents/src/serie/term01/clima.txt", 'r');
//         $cursor = -1;
// 
//         fseek($f, $cursor, SEEK_END);
//         $char = fgetc($f);
// 
//         /**
//         * Trim trailing newline chars of the file
//         */
//         while ($char === "\n" || $char === "\r") {
//             fseek($f, $cursor--, SEEK_END);
//             $char = fgetc($f);
//         }
// 
//         /**
//         * Read until the start of file or first newline char
//         */
//         while ($char !== false && $char !== "\n" && $char !== "\r") {
//             /**
//             * Prepend the new char
//             */
//             $line = $char . $line;
//             fseek($f, $cursor--, SEEK_END);
//             $char = fgetc($f);
//         }

        echo $line;
        fclose($f);

    } else
    if ($par == 'cant') {
        printf("%d",mt_rand(1, 300));
    }
}
?>


