// window.alert("Hello !") //for test purposes

function openForm(id) {
    
    if (document.getElementById(id).style.display === "block") {
        closeForm(id);
    }

    else 
        document.getElementById(id).style.display = "block";
}
  
function closeForm(id) {
    document.getElementById(id).style.display = "none";
}

function clearForm(id) {
    document.getElementById(id).reset();
}