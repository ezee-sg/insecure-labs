<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header("Location: index.php?error=noperm");
    exit;
}

require_once 'db.php';
$username = $_SESSION['username'];

$stmt = $pdo->query("SELECT id, username FROM users ORDER BY id ASC");
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel de Administración</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body style="background-color: #f8f9fa;">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">🧭 AdminPanel</a>
            <div class="d-flex">
                <span class="navbar-text text-white me-3">
                    Bienvenido, <?= htmlspecialchars($username) ?>
                </span>
                <a href="logout.php" class="btn btn-outline-light">Cerrar sesión</a>
            </div>
        </div>
    </nav>

    <div class="container mt-5">
        <h2 class="mb-4">👥 Gestión de Usuarios</h2>
        <table class="table table-bordered table-hover bg-white shadow-sm">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nombre de Usuario</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($users as $user): ?>
                <tr>
                    <td><?= htmlspecialchars($user['id']) ?></td>
                    <td><?= htmlspecialchars($user['username']) ?></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

    <footer class="text-center text-muted mt-5 mb-3">
        <small>&copy; <?= date("Y") ?> AdminPanel Inc. Todos los derechos reservados.</small>
    </footer>
</body>
</html>
