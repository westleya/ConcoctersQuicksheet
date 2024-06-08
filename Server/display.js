// code to take dummy data, store in json object, and send to server on button press.
function submitData()
{
    const xhr = new XMLHttpRequest()
    xhr.open("POST", "https://jsonplaceholder.typicode.com/todos")
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")
    xhr.onload = () => {
        if (xhr.readyState == 4 && xhr.status == 201){
            console.log(JSON.parse(xhr.responseText))
        } else {
            console.log('Error: ${xhr.status}$')
        }
    }
    let jsonobj = JSON.stringify({"eleval":element.value})
    xhr.send(jsonobj)
}
let element = document.getElementById("base price")
let button = document.getElementById("submit")
button.addEventListener("click", submitData)