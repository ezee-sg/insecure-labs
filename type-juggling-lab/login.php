<?php
session_start();
require_once 'db.php';

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$hash = md5($password);

$stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
$stmt->execute(['username' => $username]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user && $hash == $user['password']) {
    $_SESSION['logged_in'] = true;
    $_SESSION['username'] = $user['username'];
    header("Location: admin.php");
    exit;
} else {
    $message = "<div class='alert alert-danger'>❌ Acceso denegado.</div>";
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultado</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container" style="max-width: 500px; margin-top: 100px;">
        <?= $message ?>
        <a href="index.php" class="btn btn-secondary mt-3 w-100">🔙 Volver</a>
    </div>
</body>
</html>
