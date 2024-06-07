// code to take dummy data, store in json object, and send to server on button press.
function submitData()
{
    let jsonobj = {"eleval":element.value}
    
    console.log(jsonobj.eleval)
}

let element = document.getElementById("base price")
let button = document.getElementById("submit")
button.addEventListener("click", submitData)