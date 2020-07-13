var getData =function(){
    var user= document.getElementById("User").value;
    var pass= document.getElementById("Pass").value;
    console.log(user,pass)
    if(user == ""){
        document.getElementById("User").focus();
     }else{ 
        if(pass == ""){
            document.getElementById("Pass").focus();
        }
    }
}

function close_window()
{
    window.close();
}