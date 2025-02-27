const express = require("express");
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");
const path = require("path");
const session = require("express-session");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(session({
    secret: "supersecreto",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}));

app.use(express.static(path.join(__dirname, "css")));

const url = "mongodb://mongo:27017";
const dbName = "administration";

// Rutas
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "views", "login.html"));
});

app.post("/login", async (req, res) => {
    const { username, password } = req.body;

    const client = new MongoClient(url);
    try {
        await client.connect();
        const db = client.db(dbName);
        const users = db.collection("users");

        const user = await users.findOne({ username, password });

        if (user) {
            req.session.user = user;
            return res.json({ success: true, redirect: "/admin" });
        } else {
            return res.json({ success: false, message: "❌ Credenciales incorrectas." });
        }
    } catch (error) {
        return res.json({ success: false, message: "⚠️ Error en el servidor." });
    } finally {
        await client.close();
    }
});


app.get("/admin", (req, res) => {
    if (!req.session.user) {
        return res.status(403).sendFile(path.join(__dirname, "views", "error.html"));
    }
    res.sendFile(path.join(__dirname, "views", "admin.html"));
});

app.listen(port, () => {
    console.log(`🚀 Servidor corriendo en http://localhost:${port}`);
});
