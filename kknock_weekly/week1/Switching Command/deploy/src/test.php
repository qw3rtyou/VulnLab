<?php

include ("./config.php");

$pat = '/\b(flag|nc|netcat|bin|bash|rm|sh)\b/i';

if ($_SESSION["auth"] === "guest") {
    $command = "echo hi hi";
    $res = shell_exec($command);
} else if ($_SESSION["auth"] === "admin") {

    $command = isset($_GET["cmd"]) ? $_GET["cmd"] : "ls";
    $sanitized_command = str_replace("\n", "", $command);
    if (preg_match($pat, $sanitized_command)) {
        exit("hehe");
    }
    $resulttt = shell_exec(escapeshellcmd($sanitized_command));
} else {
    $res = "Who r u?";
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Command Test</title>
</head>

<body>
    <h2>Command Test</h2>
    <?php
    echo "<pre>$res</pre>";
    ?>
</body>

</html>