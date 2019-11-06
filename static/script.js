// window.alert("Hello !") //for test purposes


// ------------------------------FORM ENABLE/DISABLE-----------------------------
function disableform(formId) {
    var f = document.forms[formId].getElementsByTagName('input');
    for (var i=0;i<f.length;i++)
        f[i].disabled=true
    var f = document.forms[0].getElementsByTagName('radio');
    for (var i=0;i<f.length;i++)
        f[i].disabled=true
    var f = document.forms[0].getElementsByTagName('button');
    for (var i=0;i<f.length;i++)
        f[i].disabled=true
}

function enableform(formId) {
    var f = document.forms[formId].getElementsByTagName('input');
    for (var i=0;i<f.length;i++)
        f[i].disabled=false
    var f = document.forms[0].getElementsByTagName('radio');
    for (var i=0;i<f.length;i++)
        f[i].disabled=false
    var f = document.forms[0].getElementsByTagName('button');
    for (var i=0;i<f.length;i++)
        f[i].disabled=false
}









// --------------------------------HTML SHOW/HIDE/CHANGE---------------------------

function hide(Id) {
    
    //A function to hide elements
    
    document.getElementById(Id).style.display = "none";
}

function show(Id) {
    
    //A function to show elements
    
    document.getElementById(Id).style.display = "block";
}

function changeHTML(Id, str) {
    
    //A function to change HTML elements to given str
    
    document.getElementById(Id).innerHTML = str;
}


// -----------------------------FORM OPEN/CLOSE-----------------------------
function openForm(id) {
    
    if (document.getElementById(id).style.display === "block") {
        closeForm(id);
    }

    else 
        document.getElementById(id).style.display = "block";
}
  
function closeForm(id) {
    document.getElementById(id).reset();
    document.getElementById(id).style.display = "none";
}
