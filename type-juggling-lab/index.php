<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login - Panel de Administración</title>
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
        .alert-warning {
            background-color: #665c00;
            border-color: #665c00;
            color: #fff;
        }
        a {
            color: #4ea8de;
        }
    </style>
</head>
<body>
    <div class="container" style="max-width: 500px; margin-top: 100px;">
        <h2 class="mb-4">Iniciar Sesión</h2>
        <?php if (isset($_GET['error']) && $_GET['error'] === 'noperm'): ?>
            <div class="alert alert-warning">Debes iniciar sesión para acceder al panel.</div>
        <?php endif; ?>

        <form action="login.php" method="POST">
            <div class="mb-3">
                <label for="username" class="form-label">Usuario</label>
                <input type="text" class="form-control" name="username" id="username" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Contraseña</label>
                <input type="text" class="form-control" name="password" id="password" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Entrar</button>
        </form>
        <p class="mt-3 text-center">¿No tienes cuenta? <a href="register.php">Regístrate aquí</a></p>
    </div>
</body>
</html>
