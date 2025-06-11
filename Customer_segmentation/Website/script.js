const cart = [];

function addToCart(productName, productCategory, productPrice) {
    const product = {
        id: cart.length + 1,
        name: productName,
        category: productCategory,
        price: productPrice
    };
    fetch('/api/cart/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            productId: product.id,
            quantity: 1 // You might want to allow users to select the quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert(productName + " added to cart!");
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.product button');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const product = this.parentNode;
            const productName = product.querySelector('h3').textContent;
            const productCategory = product.querySelector('p:nth-child(2)').textContent.split(': ')[1];
            const productPrice = product.querySelector('p:nth-child(3)').textContent.split(': ')[1];
            addToCart(productName, productCategory, productPrice);
        });
    });
});

// Sample user schema
const userSchema = {
    id: 1,
    name: "John Doe",
    spendingScore: 75
};
