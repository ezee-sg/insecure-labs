<?php
include("includes/header.php");

function loadModule() {
    if (isset($_GET['module'])) {
        $module = $_GET['module'];
    } else {
        $module = "modules/default.php";
    }

    include($module);
}

loadModule();

include("includes/footer.php");
?>
