function remove (something){
    
    something.remove();
}
function pettings(element){
    element.innerHTML = parseInt(element.innerHTML)+1
    console.log(element);
    }
function disclaimer(element){
    // alert(element.innerHTML)
    // alert("k")
    var stringg = document.getElementById("scroll").value;
    alert("you are looking for a "+stringg)
}