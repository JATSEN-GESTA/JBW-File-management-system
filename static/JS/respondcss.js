function sendMail(params) {
	var tempParams = {
		from_name:document.getElementById("from_email").value,
		to_name:document.getElementById("to_email").value,
		subject:document.getElementById("sub").value,
		message:document.getElementById("msg").value,
	};

    var name = document.getElementById("from_email");
    var name2 = document.getElementById("to_email");
    var name3 = document.getElementById("sub");
    var name4 = document.getElementById("msg");
    
    if(name.value == "")
    {
        alert("Please fill up the Sender Email!");
    }
	else if(name2.value == "")
    {
        alert("Please fill up the Receiver Email!");
    }
    else if(name3.value == "")
    {
        alert("Please fill up the Subject!");
    }
    else if(name4.value == "")
    {
        alert("Please fill up the Message!");
    }
    else
	{
		var userval = confirm("Are you sure you want to submit?");
		if(userval == true){
			emailjs.send('service_9mzjoac', 'template_110rix7', tempParams)
			.then((message) => alert("Mail sent succesfully"));
	
			document.getElementById("from_email").value = null;
			document.getElementById("to_email").value = null;
			document.getElementById("sub").value = null;
			document.getElementById("msg").value = null;
			
		}


	}

	}