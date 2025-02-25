<?php

$dir = 'uploads/';
$images = scandir($dir);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repositorio de Imágenes</title>
    <link rel="stylesheet" href="static/index.css">
</head>
<body>
    <div class="container">
        <h1>Repositorio de Imágenes</h1>
        
        <div class="grid-container">
            <?php
            foreach ($images as $image) {
                if ($image !== '.' && $image !== '..') {
                    echo '<div class="grid-item">';
                    echo '<img src="' . $dir . $image . '" alt="' . $image . '">';
                    echo '<a href="show_image.php?image=' . urlencode($image) . '" class="btn">Ver Imagen</a>';
                    echo '</div>';
                }
            }
            ?>
        </div>
        
        <a href="upload_image.php" class="btn-upload">Subir Imagen</a>
    </div>
</body>
</html>
