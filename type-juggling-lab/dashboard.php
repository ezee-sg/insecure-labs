<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header("Location: index.php?error=noperm");
    exit;
}

require_once 'db.php';
$username = $_SESSION['username'];
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Dashboard Personal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #fff;
        }
        .sidebar {
            height: 100vh;
            background-color: #1e1e1e;
            padding: 20px;
            position: fixed;
            top: 0;
            left: 0;
            width: 220px;
        }
        .sidebar h4 {
            color: #ccc;
        }
        .sidebar a {
            color: #aaa;
            display: block;
            padding: 10px;
            text-decoration: none;
            margin-bottom: 5px;
            border-radius: 4px;
        }
        .sidebar a:hover {
            background-color: #333;
            color: #fff;
        }
        .main-content {
            margin-left: 240px;
            padding: 40px 20px;
        }
        .table {
            background-color: #1e1e1e;
            color: #fff;
        }
        .table th,
        .table td {
            border-color: #333;
        }
        .table-hover tbody tr:hover {
            background-color: #2a2a2a;
        }
        .table-dark {
            background-color: #212529;
        }
        .shadow-sm {
            box-shadow: 0 .125rem .25rem rgba(255,255,255,.075)!important;
        }
        .navbar-dark .navbar-brand,
        .navbar-dark .navbar-text {
            color: #ffffff;
        }
        footer {
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <h4>Dashboard</h4>
        <a href="#">Inicio</a>
        <a href="#">Mis Estadísticas</a>
        <a href="#">Crear Nuevo Proyecto</a>
        <a href="#">Ver Mis Archivos</a>
        <a href="#">Configuración</a>
        <hr>
        <a href="logout.php" class="text-danger">Cerrar sesión</a>
    </div>

    <div class="main-content">
        <nav class="navbar navbar-dark bg-dark rounded shadow-sm mb-4">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Bienvenido, <?= htmlspecialchars($username) ?></a>
            </div>
        </nav>

        <h2 class="mb-4">Tu Dashboard</h2>
        <div class="row">
            <div class="col-md-6">
                <h4>Estadísticas</h4>
                <p>Aquí se mostrarían estadísticas de uso, proyectos, o datos personalizados del usuario.</p>
                <button class="btn btn-secondary" disabled>Ver Estadísticas</button>
            </div>
            <div class="col-md-6">
                <h4>Mis Archivos</h4>
                <p>Podrías ver tus archivos aquí, pero actualmente no hay ninguno.</p>
                <button class="btn btn-secondary" disabled>Ver Archivos</button>
            </div>
        </div>

        <h4 class="mt-5">Funciones No Habilitadas</h4>
        <p>El sistema está en desarrollo, pero en el futuro podrás:</p>
        <ul>
            <li>Crear nuevos proyectos</li>
            <li>Ver estadísticas detalladas</li>
            <li>Gestionar tus archivos y documentos</li>
            <li>Configurar tus preferencias</li>
        </ul>
    </div>
</body>
</html>
