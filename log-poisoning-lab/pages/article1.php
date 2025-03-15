<?php

$title = "La importancia de la autenticación multifactor";
$content = "
    <p>La autenticación multifactor (MFA) es una técnica de seguridad que requiere que los usuarios proporcionen dos o más verificaciones 
    de identidad antes de acceder a un sistema. Esta capa adicional de seguridad ayuda a proteger las cuentas contra los ataques, 
    especialmente contra los ataques de phishing y el robo de contraseñas.</p>

    <img src='images/articulo1.png' alt='Autenticación Multifactor'>

    <p>Existen varios factores que se pueden usar en la autenticación multifactor:</p>
    <ul>
        <li><strong>Algo que sabes:</strong> una contraseña o PIN.</li>
        <li><strong>Algo que tienes:</strong> un teléfono móvil, tarjeta de seguridad o dispositivo de hardware.</li>
        <li><strong>Algo que eres:</strong> huella dactilar, reconocimiento facial o escaneo de iris.</li>
    </ul>

    <p>La MFA es una de las mejores formas de proteger las cuentas en línea, y su implementación en plataformas de correo electrónico, 
    redes sociales y servicios bancarios es altamente recomendada. En caso de que un atacante obtenga una contraseña, la MFA todavía 
    bloquearía el acceso si no tiene el segundo factor.</p>
";
echo "<h2>" . $title . "</h2>";
echo $content;
?>
