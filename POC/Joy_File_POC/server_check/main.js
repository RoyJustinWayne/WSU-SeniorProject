// ajax call to check server status from client side to AWS 
//this is just a test from front-end side

var statusContainer = document.getElementById("status");
var btn = document.getElementById("btn");
// btn.addEventListener("click", function(){

//     var ourRequest = new XMLHttpRequest();
//     ourRequest.open('GET', 'AWS-API');
//     ourRequest.onload = function(){
//         var ourData = JSON.parse(ourRequest.responseText);
//         // console.log(ourData);
//         renderHTML(ourData);
//     };
//     ourRequest.send();
// });

var myVar = setInterval(check_server, 5000);

function check_server(){

    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'AWS-API');
    ourRequest.onload = function(){
        var ourData = JSON.parse(ourRequest.responseText);
        // console.log(ourData);
        renderHTML(ourData);
    };
    ourRequest.send();
}


function renderHTML(data){
    var htmlString = data.server;
    if (htmlString == 'OK'){
        // statusContainer.insertAdjacentHTML('beforeend', 'OK');
        statusContainer.innerHTML = "OK";
        // document.getElementById("status").value= new String(htmlString);
    }
    else {
        statusContainer.innerHTML = "NOT OK";
    }
    
}