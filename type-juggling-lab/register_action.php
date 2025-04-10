<?php
require_once 'db.php';

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$hash = md5($password);

$stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:u, :p)");
try {
    $stmt->execute(['u' => $username, 'p' => $hash]);
    $message = "<div class='alert alert-success'>✅ Usuario $username registrado correctamente!></div>";
} catch (PDOException $e) {
    $message = "<div class='alert alert-danger'>❌ Error: " . $e->getMessage() . "</div>";
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container" style="max-width: 500px; margin-top: 100px;">
        <?= $message ?>
        <a href="index.php" class="btn btn-primary mt-2 w-100">🔑 Ir al login</a>
    </div>
</body>
</html>
