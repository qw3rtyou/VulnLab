<?php
require ("secret.php");

$input_code = $_POST['access_code'];
$hash = hash('sha256', $input_code);

session_start();
if ($hash === SECRET_KEY) {
    $_SESSION['admin'] = true;
    echo "An access code has been issued upon correct access.";
    echo "Administrator privileges have been granted.";
} else {
    echo "<script>alert('The access code is incorrect. Administrator registration is only possible on local host.');</script>";
    echo "<script>location.href='/index.php'</script>";
}


$admin_token = $row["content"];
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    include "./templates/admin.html";
} else if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
    } catch (Exception $e) {
        echo "<script>alert('Wrong.');</script>";
        echo "<script>location.href='/index.php'</script>";
    }
} else {
    echo "<script>alert('This is an unusual approach.');</script>";
    echo "<script>location.href='/index.php'</script>";
}
?>