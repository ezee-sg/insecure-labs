<?php
session_start();
$current_page = basename($_SERVER['PHP_SELF']);
?>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.php">InsecureNet</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-center w-100" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'index.php') ? 'active-link' : ''; ?>" href="index.php">Inicio</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'profile.php') ? 'active-link' : ''; ?>" href="profile.php">Ver Perfil</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'friends.php') ? 'active-link' : ''; ?>" href="friends.php">Amigos</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'messages.php') ? 'active-link' : ''; ?>" href="messages.php">Mensajes</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?php echo ($current_page == 'settings.php') ? 'active-link' : ''; ?>" href="settings.php">Configuración</a>
                </li>
            </ul>
        </div>

        <div class="d-flex align-items-center ms-auto">
            <?php if (isset($_SESSION['username'])): ?>
                <span class="text-white me-3"><?php echo $_SESSION['username']; ?></span>
                <a href="logout.php" class="btn btn-outline-danger ms-2">Cerrar sesión</a>
            <?php else: ?>
                <a href="login.php" class="btn btn-outline-light ms-2">Iniciar sesión</a>
            <?php endif; ?>
        </div>

    </div>
</nav>
