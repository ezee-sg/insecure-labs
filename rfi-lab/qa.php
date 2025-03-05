<?php
include("includes/header.php");

$qa = [
    "Curso de PHP Básico" => [
        ["¿Qué es PHP?", "PHP es un lenguaje de programación de servidor usado para crear sitios web dinámicos."],
        ["¿Qué diferencias hay entre include y require?", "Ambos incluyen archivos en PHP, pero require detendrá la ejecución si el archivo no existe, mientras que include solo mostrará una advertencia."]
    ],
    "Curso de JavaScript para Principiantes" => [
        ["¿Qué es JavaScript?", "JavaScript es un lenguaje de programación utilizado para crear interactividad en sitios web."],
        ["¿Cuál es la diferencia entre var, let y const?", "var es una declaración global, let y const tienen un alcance de bloque, pero const no puede ser reasignado."]
    ]
];
?>

<div class="content">
    <h2>Preguntas y Respuestas</h2>
    <?php foreach ($qa as $course => $questions): ?>
        <h3><?php echo htmlspecialchars($course); ?></h3>
        <ul>
            <?php foreach ($questions as $q): ?>
                <li>
                    <strong><?php echo htmlspecialchars($q[0]); ?></strong><br>
                    <?php echo htmlspecialchars($q[1]); ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endforeach; ?>
</div>

<?php
include("includes/footer.php");
?>
