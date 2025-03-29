<?php
$host = "file-upload-db";
$user = "root";
$pass = "root";
$dbname = "social_network";

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>
