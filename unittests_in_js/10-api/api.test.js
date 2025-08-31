const { expect } = require('chai');

describe('Index page', function () {
    it('should return correct status code and body', async function () {
        const res = await fetch('http://localhost:7865/');
        const text = await res.text();

        expect(res.status).to.equal(200);
        expect(text).to.equal('Welcome to the payment system');
    });
});

describe('Cart page', function () {
    it('should return 200 and correct body when id is a number', async function () {
        const res = await fetch('http://localhost:7865/cart/123');
        const text = await res.text();

        expect(res.status).to.equal(200)
        expect(text).to.equal('Payment methods for cart 123');
    });
    it('should return 404 when id is not a number', async function () {
        const res = await fetch('http://localhost:7865/cart/xd');
        const text = await res.text()

        expect(res.status).to.equal(404)
        expect(text).to.equal('Invalid cart id')
    })
});

describe('Login endpoint', function () {
    it('should return welcome message with correct name', async function () {
        const res = await fetch('http://localhost:7865/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userName: 'Santiwi' })
        })
        const text = await res.text()

        expect(res.status).to.equal(200)
        expect(text).to.equal('Welcome Santiwi')
    })
});

describe('available payments endopint', function () {
    it('should return correct object', async function () {
        const res = await fetch('http://localhost:7865/available_payments')
        const json = await res.json()

        expect(res.status).to.equal(200)
        expect(json).to.deep.equal({
            payment_methods: {
                credit_cards: true,
                paypal: false
            }
        })
    })
})