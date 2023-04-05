function getPassword (){
   
    var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 
    'abcdefghijklmnopqrstuvwxyz0123456789@#$';;

    var passwordLenght = 12;
    var passwordgen = ""
    for (var i=0; i<passwordLenght; i++){
        console.log(i)
        var randomNumber = Math.floor(Math.random()* chars.length)
        passwordgen +=chars.substring(randomNumber, randomNumber +1);


    }
    console.log(passwordgen)
    document.getElementById("pass").value = passwordgen
}
function toggleInput() {
    // get the value of the select element
    var select = document.getElementById("getposition");
    console.log(select)
    var selectedValue = select.value;
    console.log("the selected value is", selectedValue)
    // get the input field
    var input = document.getElementById("input");
    if (selectedValue == "GH/DH") {
        selectghdh.style.display = "none"


    }   
    else{
        selectghdh.style.display = "block"
    }
    if (selectedValue == "Tech Director") {
        select_tech.style.display = "none"


    }    
    else{
        select_tech.style.display = "block"
    }
  }


// function showpass(){
//     console.log("hello hello from password")
//     const passvalud = document.getElementById("hidepass")
//     console.log("innerhtml is ",passvalud.innerHTML)
//     // var data = document.getElementById("hidepass").innerHTML;
//     // console.log(data)
//     if (passvalud.innerHTML == "Show Password"){
//         console.log("helloshow")
//         passvalud.setAttribute("type", "text")
//         console.log(passvalud)
        
//     }
//     if (passvalud.innerHTML == "Hide Password"){
//         console.log("helohide")
//         passvalud.setAttribute("type","password")
//         passvalud.innerHTML = "Show Password"

        
//     }
    


// }
const mySelect = document.getElementById('mySelect');

mySelect.addEventListener('change', () => {
  const selectedValue = mySelect.value;
  console.log("on change")
  console.log(selectedValue);
});

function togglePassword() {
    var passwordField = document.getElementById("passwordField");
    var button = document.getElementById("hidepass")
    if (passwordField.type === "password") {
      passwordField.type = "text";
      button.innerHTML = "Hide Password"
      
    } else {
      passwordField.type = "password";
      button.innerHTML = "Show Password"
    }
  }

function deleteItem(itemId) {
    if (confirm('Are you sure you want to delete this item?')) {
      window.location.href = '/adminpanel/delete-user/' + itemId;
    }
   
  }