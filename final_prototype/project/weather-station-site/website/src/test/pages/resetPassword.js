const webdriver = require('selenium-webdriver');
const {Builder, By, Key, until} = require('selenium-webdriver');

module.exports = function(driver) {
    const elements = {
        emailInput: By.css('#email'),
        recoverButton: By.css('.recover-btn'),
        returnButton: By.css('.return-btn'),
    };
    return {
        url:  'http://loadbalancer-joy-final-1171049135.us-east-1.elb.amazonaws.com/user/reset',
        elements: elements,
        waitUntilVisible: function() {
            return driver.wait(until.elementLocated(elements.usernameInput));
        },
        navigate: function() {
            driver.navigate().to(this.url);
            return this.waitUntilVisible();
        },
        enterEmail: function(value) {
            return driver.findElement(elements.emailInput).sendKeys(value);
        },
        getEmail: function() {
            return driver.findElement(elements.emailInput).getAttribute('value')
        },
        recover: function(){
            return driver.findElement(elements.recoverButton).click();
        },
        return: function(){
            return driver.findElement(elements.returnButton).click();
        },
    };
};