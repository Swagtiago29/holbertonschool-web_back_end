const { expect } = require('chai');
const app = require('./api');

let server;

describe('Index page', function () {
  before((done) => {
    // Start server before tests
    server = app.listen(7865, done);
  });

  after((done) => {
    // Close server after tests
    server.close(done);
  });

  it('should return correct status code and body', async function () {
    const res = await fetch('http://localhost:7865/');
    const text = await res.text();

    expect(res.status).to.equal(200);
    expect(text).to.equal('Welcome to the payment system');
  });
});
