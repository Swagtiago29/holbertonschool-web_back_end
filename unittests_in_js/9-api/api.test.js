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

