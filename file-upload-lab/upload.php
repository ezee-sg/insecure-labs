<?php
include 'auth.php';
include 'db.php';

$user_id = $_SESSION['user_id'];

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["profile_pic"])) {
    $upload_dir = "uploads/";
    
    $file_tmp = $_FILES["profile_pic"]["tmp_name"];
    $file_name = basename($_FILES["profile_pic"]["name"]);
    $file_path = $upload_dir . $file_name;

    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mime_type = finfo_file($finfo, $file_tmp);
    finfo_close($finfo);

    $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
    if (!in_array($_FILES["profile_pic"]["type"], $allowed_types) || !in_array($mime_type, $allowed_types)) {
        die("Error: Tipo de archivo no permitido.");
    }

    if (move_uploaded_file($file_tmp, $file_path)) {
        $stmt = $conn->prepare("UPDATE users SET profile_pic = ? WHERE id = ?");
        if ($stmt) {
            $stmt->bind_param("si", $file_path, $user_id);
            $stmt->execute();
            $stmt->close();
        }

        header("Location: profile.php");
        exit();
    } else {
        die("Error al subir la imagen.");
    }
} else {
    die("No se ha subido ningún archivo.");
}
?>
