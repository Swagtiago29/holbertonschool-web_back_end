const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get(`/cart/:id`, (req, res) => {
    const id = req.params.id

    if (!/^\d+$/.test(id)) {
        return res.status(404).send('Invalid cart id')
    }
    return res.send(`Payment methods for cart ${id}`)
})
// Only start server if run directly
if (require.main === module) {
    const PORT = 7865;
    app.listen(PORT, () => {
        console.log(`API available on localhost port ${PORT}`);
    });
}

module.exports = app; // export app for tests
