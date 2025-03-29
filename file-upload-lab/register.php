<?php
session_start();
include 'db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $description = $_POST['description'];

    $stmt = $conn->prepare("INSERT INTO users (name, username, password, email, description) VALUES (?, ?, ?, ?, ?)");

    if (!$stmt) {
        die("Error en la consulta: " . $conn->error);
    }

    $stmt->bind_param("sssss", $name, $username, $password, $email, $description);
    
    if ($stmt->execute()) {
        header("Location: login.php");
        exit();
    } else {
        $error = "Error al registrar usuario. Puede que el usuario ya exista.";
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="card mx-auto" style="max-width: 400px;">
            <div class="card-body">
                <h2 class="text-center">Registro</h2>
                <?php if (isset($error)) echo "<p class='text-danger text-center'>$error</p>"; ?>
                <form method="POST">
                    <div class="mb-3">
                        <label for="name" class="form-label">Nombre Completo</label>
                        <input type="text" class="form-control" id="name" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="username" class="form-label">Usuario</label>
                        <input type="text" class="form-control" id="username" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Correo Electrónico</label>
                        <input type="email" class="form-control" id="email" name="email" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Contraseña</label>
                        <input type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="form-label">Descripción</label>
                        <textarea class="form-control" id="description" name="description" rows="3" placeholder="Escribe algo sobre ti"></textarea>
                    </div>
                    <button type="submit" class="btn btn-success w-100">Registrarse</button>
                </form>
                <p class="text-center mt-3">
                    ¿Ya tienes cuenta? <a href="login.php">Inicia sesión aquí</a>
                </p>
            </div>
        </div>
    </div>
</body>
</html>
