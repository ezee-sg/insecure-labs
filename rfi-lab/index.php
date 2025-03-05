<?php
$courses = [
    [
        'title' => 'Curso de PHP Básico',
        'description' => 'Aprende los fundamentos de PHP, desde las bases hasta conceptos más avanzados.',
        'link' => 'course.php?module=modules/php-course.php'
    ],
    [
        'title' => 'Curso de JavaScript para Principiantes',
        'description' => 'Conoce los fundamentos de JavaScript, creando aplicaciones dinámicas para la web.',
        'link' => 'course.php?module=modules/js-course.php'
    ]
];

include("includes/header.php");
?>

<div class="content">
    <h2>Nuestros Cursos</h2>
    <div class="course-list">
        <?php foreach ($courses as $course): ?>
            <div class="course-item">
                <h3><?php echo htmlspecialchars($course['title']); ?></h3>
                <p><?php echo htmlspecialchars($course['description']); ?></p>
                <a href="<?php echo $course['link']; ?>">Ver más</a>
            </div>
        <?php endforeach; ?>
    </div>
</div>

<?php
include("includes/footer.php");
?>
