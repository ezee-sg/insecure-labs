db = db.getSiblingDB("administration");

db.createCollection("users");

db.users.insertOne(
    { username: "admin", password: "admin123", role: "admin" }
);
