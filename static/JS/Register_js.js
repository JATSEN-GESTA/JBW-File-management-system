    var usernameArray=[];
    var passwordArray=[];

    function register(){

        var username1 = document.getElementById("fuser").value;
        var password1 = document.getElementById("fpass").value;
        var passwordRetype = document.getElementById("fcpass").value;

        if (username1 == ""){
            alert("Username required.");
            return ;
        }
        else if (password1 == ""){
            alert("Password required.");
            return ;
        }
        else if (passwordRetype == ""){
            alert("Confirm Password required.");
            return ;
        }
        else if ( password1 != passwordRetype ){
            alert("Password don't match retype your Password.");
            return;
        }
        else if(usernameArray.indexOf(username1) == -1){
            usernameArray.push(username1);
            passwordArray.push(password1);

            alert(username1 + "  Thanks for registration. \nTry to login Now");

            document.getElementById("fuser").value ="";
            document.getElementById("fpass").value="";
            document.getElementById("fcpass").value="";
            window.location = "Login.html";
        }
        else{
            alert(email + " is already register.");
            return ;
        }
         
    }