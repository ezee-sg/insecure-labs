<?php
include("includes/header.php");

$page = $_GET['page'] ?? 'home.php';

include("pages/" . $page);

include("includes/footer.php");
?>
