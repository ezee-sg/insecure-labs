<?php
$uploads_dir = 'uploads/';

if (isset($_GET['image'])) {
    $image = $_GET['image'];
    $file_path = $uploads_dir . $image;

    if (file_exists($file_path)) {
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . basename($file_path) . '"');
        header('Content-Length: ' . filesize($file_path));

        readfile($file_path);
        exit;
    } else {
        echo "La imagen no se encuentra o hubo un error en la descarga.";
    }
}
?>
