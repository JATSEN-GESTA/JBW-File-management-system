var usernameArray = ["user", "Jatsen Gesta", "Wendell Magdaluyo", "Bryan Batuigas"];
var passwordArray = ["user", "123456", "123456", "123456"];

function CustomerlOGIN(){

    var username = document.getElementById("fuser").value;
    var password = document.getElementById("fpass").value;

    var i = usernameArray.indexOf(username);

    if(usernameArray.indexOf(username) == -1){
        if (username == ""){
            alert("Username required.");
            return ;
        }
        alert("Username does not exist.");
        return ;
    }
    else if(passwordArray[i] != password){
        if (password == ""){
            alert("Password required.");
            return ;
        }
        alert("Password does not match.");
        return ;
    }
    else {
        alert(username + " you are login Now \n welcome to our website.");

        document.getElementById("fuser").value ="";
        document.getElementById("fpass").value="";
        window.location = "{% url 'mainwindow' %}";
    }
}