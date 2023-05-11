function logout(element){
    if (element.innerText=="logout"){
        element.innerText="login"
    }
    else {
    element.innerText="logout"
    }
}
function hide(element){
    element.remove()
}
function like(){alert("Ninja was liked")}