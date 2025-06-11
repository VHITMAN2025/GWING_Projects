const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 3000;

app.use(express.json());

// MySQL Connection
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'HITMAN2025',
    database: 'ecommerce',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// Test the database connection
pool.getConnection((err, connection) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
    } else {
        console.log('Connected to MySQL database!');
        connection.release();
    }
});

// API endpoint to get all products
app.get('/api/products', (req, res) => {
    pool.query('SELECT * FROM products', (err, results) => {
        if (err) {
            console.error('Error querying products:', err);
            res.status(500).json({ error: 'Failed to retrieve products' });
        } else {
            res.json(results);
        }
    });
});

// API endpoint to add a product to the cart
app.post('/api/cart/add', (req, res) => {
    const { productId, quantity } = req.body;

    // You would typically validate the product ID and quantity here

    // For simplicity, let's assume the product ID and quantity are valid
    // In a real application, you would interact with the database to add the product to the cart

    console.log(`Product ID: ${productId}, Quantity: ${quantity}`);
    res.json({ message: 'Product added to cart successfully' });
});

app.use(express.static('.'));

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
