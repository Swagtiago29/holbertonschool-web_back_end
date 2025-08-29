const { expect } = require('chai');
const app = require('./api');

describe('Index page', function () {
    it('should return correct status code', function (done) {
        request(app)
            .get('/')
            .expect(200, done)
    });

    it('should return correct result', function (done) {
        request(app)
            .get('/')
            .end((err, res) => {
                expect(res.text).to.equal('Welcome to the payment system');
                done();
            });
    });

    it('should return the correct content type', function (done) {
        request(app)
            .get('/')
            .expect('Content-Type', /html/)
            .end(done)
    })
})