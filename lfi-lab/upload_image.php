<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["image"]["name"]);
    $imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

    if ($imageFileType !== "png" && $imageFileType !== "jpeg" && $imageFileType !== "jpg") {
        echo "Solo se permiten archivos PNG y JPEG.";
        exit;
    }

    if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
        echo "La imagen ". htmlspecialchars(basename($_FILES["image"]["name"])) . " ha sido subida exitosamente.";
    } else {
        echo "Lo siento, ocurrió un error al subir tu imagen.";
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subir Imagen</title>
    <link rel="stylesheet" href="static/upload_image.css">
</head>
<body>
    <a href="index.php" class="btn-back">Volver al Repositorio</a>
    <h1>Subir Imagen (Solo PNG o JPEG)</h1>
    <div class="container">
        <form action="upload_image.php" method="post" enctype="multipart/form-data">
            <input type="file" name="image" required>
            <input type="submit" value="Subir Imagen" class="btn">
        </form>
    </div>
</body>
</html>
