<?php
$uploads_dir = 'uploads/';
if (isset($_GET['image'])) {
    $image = $_GET['image'];
    $file_path = $uploads_dir . $image;

    if (file_exists($file_path)) {
        echo "<div class='container'>";
        echo "<h2>Imagen: " . htmlspecialchars($image) . "</h2>";
        echo "<img src='" . $file_path . "' alt='Imagen subida' class='image-preview'><br>";
        echo "<a href='download_image.php?image=" . urlencode($image) . "' class='btn'>Descargar</a>";
        echo "</div>";
    } else {
        echo "<div class='container'>La imagen no existe o no se ha subido correctamente.</div>";
    }
}
?>


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ver Imagen</title>
    <link rel="stylesheet" href="static/show_image.css">
</head>
<body>
    <a href="index.php" class="btn-back">Volver al Repositorio</a>
</body>
</html>
