const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get(`/cart/:id`, (req, res) => {
    const id = req.params.id

    if (!/^\d+$/.test(id)) {
        return res.status(404).send('Invalid cart id')
    }
    return res.send(`Payment methods for cart ${id}`)
});

app.get('/available_payments', (req, res) => {

    return res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', (req, res) => {
    const { userName } = req.body
    return res.send(`Welcome ${username}`)
})

// IMPORTANT Only start server if run directly
if (require.main === module) {
    const PORT = 7865;
    app.listen(PORT, () => {
        console.log(`API available on localhost port ${PORT}`);
    });
}

module.exports = app;
