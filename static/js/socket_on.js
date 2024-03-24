socket.on('click-on-key', function(msg) {
    let divId = msg['div_id'] + '-value'
   document.getElementById(divId).innerHTML = msg['html'];
});



socket.on('click-on-value', function(msg) {

    let newHTML = "<div id='level"+msg["div_id"]
    newHTML +="-block' class='level-div'><div id='level"+msg["div_id"]
    newHTML+= "-key'></div><div id='level"+msg["div_id"]
    newHTML += "-value'></div></div>"

    document.getElementById("main-div").innerHTML += newHTML;

    let newId = 'level'+msg["div_id"]
   document.getElementById(newId+'-key').innerHTML = msg['html'];
});