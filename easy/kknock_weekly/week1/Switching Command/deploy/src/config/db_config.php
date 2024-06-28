<?php
$conn = mysqli_connect("db", "ftzhackerschool", "ftzhackerschool", "ftzhackerschool");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>