const { expect } = require('chai');

describe('Index page', function () {
  it('should return correct status code and body', async function () {
    const res = await fetch('http://localhost:7865/');
    const text = await res.text();

    expect(res.status).to.equal(200);
    expect(text).to.equal('Welcome to the payment system');
  });
});
