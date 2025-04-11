<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .form-control {
            background-color: #1e1e1e;
            color: #ffffff;
            border-color: #444;
        }
        .form-control:focus {
            background-color: #1e1e1e;
            color: #ffffff;
            border-color: #888;
        }
        .btn-secondary {
            background-color: #333;
            border-color: #555;
        }
        .btn-secondary:hover {
            background-color: #444;
        }
        a {
            color: #4ea8de;
        }
    </style>
</head>
<body>
    <div class="container" style="max-width: 500px; margin-top: 100px;">
        <h2 class="mb-4">Registro de usuario</h2>
        <form action="register_action.php" method="POST">
            <div class="mb-3">
                <label for="username" class="form-label">Usuario</label>
                <input type="text" class="form-control" name="username" id="username" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Contraseña</label>
                <input type="text" class="form-control" name="password" id="password" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Registrar</button>
        </form>
        <a href="index.php" class="btn btn-secondary mt-3 w-100">Volver al login</a>
    </div>
</body>
</html>
