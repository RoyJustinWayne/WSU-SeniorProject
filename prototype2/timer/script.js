var timeBegan = null, 
timeStopped = null, 
stopTime = 0,
started = null, 
running = false,
timeFormat = '00:00:00.000';

// starts a Vue by creating a new Vue instance with the Vue function
// registering an time format component 
// look for an existing element in the DOM with #clock to use as it's associated element when mounting.
var clock = new Vue({
    el: '#clock',
    data: {
      time: timeFormat
    }
  });
    
  document.getElementById("start").addEventListener("click", startTimer);
  document.getElementById("stop").addEventListener("click", stopTimer);
  document.getElementById("reset").addEventListener("click", resetTimer);
  
  function startTimer() {
    if(running) return;
    
    if (timeBegan === null) {
      reset();
      timeBegan = new Date();
    }
  
    if (timeStopped !== null) {
      stopTime += (new Date() - timeStopped);
    }
  
    started = setTime(clockRunning, 10);	
    running = true;
  }
  
  function stopTimer() {
    running = false;
    timeStopped = new Date();
    clearTime(started);
  }
  
  function resetTimer() {
    running = false;
    clearTime(started);
    stopTime = 0;
    timeBegan = null;
    timeStopped = null;
    clock.time = "00:00:00.000";
  }
  
  function clockRunning(){
    var currentTime = new Date(),
    timeElapsed = new Date(currentTime - timeBegan - stopTime),
    hour = timeElapsed.getUTCHours(), 
    min = timeElapsed.getUTCMinutes(), 
    sec = timeElapsed.getUTCSeconds(), 
    ms = timeElapsed.getUTCMilliseconds();
  
    clock.time = 
      timer(hour, 2) + ":" + 
      timer(min, 2) + ":" + 
      timer(sec, 2) + "." + 
      timer(ms, 3);
  };
  
  function timer(num, placeHolder) {
    var zero = '';
    for(var i = 0; i < placeHolder; i++) {
      zero += '0';
    }
    return (zero + num).slice(-placeHolder);
  }