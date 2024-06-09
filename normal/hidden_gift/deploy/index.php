<?php

include "config.php";

$page = $_REQUEST["p"];
if (!$page) {
    $page = "hello";
}

if ($page[0] === '/' || preg_match("/^.*(\\.\\.|:\\/\\/|php).*$/i", $page)) {
    die("no hack");
}

include "$page.php";