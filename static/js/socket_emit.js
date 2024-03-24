

function clickOnKey(elem){
    let value = elem.children[0].innerText
    value = value.split("(")[0]
    elem.parentNode.parentNode.parentNode.children[0].innerHTML = value.split("(")[0];
    let divId = readBlockId(elem);
    deleteDivs(divId);
    let filters = readFilters();
    if(divId=='level1') filters = [];
    console.log({'div_id': divId, 'value':value, 'filters':filters})
    socket.emit('click-on-key', {'div_id': divId, 'value':value, 'filters':filters})
}


function clickOnValue(elem, name){
    let value = elem.children[0].innerText
    value = value.split("(")[0]
    elem.parentNode.parentNode.parentNode.children[0].innerHTML = value;
    let filters = readFilters();
    let divId = readBlockId(elem)
    deleteDivs(divId);
    console.log({'div_id':divId, 'filters':filters, 'value':value})
    socket.emit('click-on-value', {'div_id':divId, 'filters':filters, 'value':value})
}


