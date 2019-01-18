const webdriver = require('selenium-webdriver');
const {Builder, By, Key, until} = require('selenium-webdriver');
const test = require('selenium-webdriver/testing');
const chai = require('chai');
const chaiWebDriver = require('chai-webdriver');

const driver = new webdriver.Builder()
    .forBrowser('chrome')
    .build();
chai.use(chaiWebDriver(driver));

const loginPage = require('./pages/login.js')(driver);

describe('Station page selenium tests', () => {
    before(function(done) {
        this.timeout(10000); // Default timeout for mocha is too short for selenium
        driver.navigate().to('http://loadbalancer-joy-final-1171049135.us-east-1.elb.amazonaws.com/')
        loginPage.enterUsername('test');
        loginPage.enterPassword('testing123');
        loginPage.login()
        .then(() => done())
    });

    it('Navigate to station health page', function(done) {
        driver.navigate().to('http://loadbalancer-joy-final-1171049135.us-east-1.elb.amazonaws.com/health');
        driver.wait(until.elementLocated(By.className('station-detail-container')), 10000).then(()=>{
            driver.findElement(By.className('station-detail-container'))
        })
        .then(() => done())
    });

    it('List view', function(done) {
        driver.wait(until.elementLocated(By.id('list-content-id')), 10000);
        driver.findElement(By.id('list-content-id'))
        .then(() => done())
    });

    it('Grid view', function(done) {
        driver.findElement(By.css('#grid-view-btn')).click();
        driver.wait(until.elementLocated(By.id('grid-content-id')), 10000).then(()=>{
            driver.findElement(By.id('grid-content-id'))
        })
        .then(() => done())
    });

    it('Open station details', function(done) {
        driver.findElement(By.css('.station-card')).click();
        driver.wait(until.elementLocated(By.css('.station-detail-modal'))).then(()=>{
            driver.findElement(By.css('.station-detail-modal'))
        })
        .then(() => done())
    });

    it('Filter stations', function(done){
        var filter = "test";
        driver.findElement(By.css('#stationFilter')).sendKeys(filter);
        
        // Needs to sleep first to give the filter time to filter out stations
        driver.sleep(150).then(() => {
            // Find all elements with this css class
            driver.findElements(By.css('.station-name-inner')).then((elements) => {
                var flag = true;
                // Iterate through our elements and check if their text is not equal to our filter
                // If the text isn't equal to our filter, it means the filter broke so we'll timeout the test
                for (var i = 0; i < elements.length; i++){
                    elements[i].getAttribute('innerHTML').then((text) => {
                        if (!text.toLowerCase().includes(filter)) flag = false;
                    }); 
                }
                if (flag === true) done();
            }) 
        });
    });

    after(function(done) {
        driver.quit().then(() => done())
    });
});