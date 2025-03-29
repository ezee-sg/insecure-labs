<?php
include 'auth.php';
include 'db.php';

$user_id = $_SESSION['user_id'];
$stmt = $conn->prepare("SELECT username, email, profile_pic, name, description FROM users WHERE id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$user = $stmt->get_result()->fetch_assoc();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Perfil</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <?php include 'header.php'; ?>

    <div class="container mt-5">
        <div class="card mx-auto" style="max-width: 600px;">
            <div class="card-body text-center">
                <h2 class="card-title"><?php echo htmlspecialchars($user['name']); ?></h2>
                
                <img src="<?php echo htmlspecialchars($user['profile_pic']); ?>" class="rounded-circle mb-3" width="150" height="150" alt="Perfil">

                <p><strong>Email:</strong> <?php echo htmlspecialchars($user['email']); ?></p>
                <p><strong>Usuario:</strong> <?php echo htmlspecialchars($user['username']); ?></p>

                <p><strong>Descripción:</strong> <?php echo nl2br(htmlspecialchars($user['description'])); ?></p>

                <form action="upload.php" method="POST" enctype="multipart/form-data">
                    <div class="mb-3">
                        <label for="profile_pic" class="form-label">Actualizar imagen de perfil</label>
                        <input type="file" class="form-control" id="profile_pic" name="profile_pic" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Actualizar Imagen</button>
                </form>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
