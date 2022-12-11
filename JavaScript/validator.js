function validate(e){
    const name=document.getElementById("name").value;
    const mobile=document.getElementById("mobile").value;
    const email=document.getElementById("email").value;
    const password=document.getElementById("password").value;
    const password2=document.getElementById("password2").value;

    console.log(name,mobile,email,password,password2);

    const name_error=document.getElementById("name_error");
    const mobile_error=document.getElementById("mobile_error");
    const email_error=document.getElementById("email_error");
    const password_error=document.getElementById("password_error");
    const password2_error=document.getElementById("password2-error");
    
    let error=false;

    if(name===""){
        name_error.innerHTML="Name is required";
        error=true;
    }
    else{
        name_error.innerHTML="";
    }

    if(mobile===""){
        mobile_error.innerHTML="MobileNo is required";
        error=true;
    }
    else if(isNaN(mobile)||mobile.length!=10){
        mobile_error.innerHTML="Please enter 10 digit valid mobile number";
        error=true;
    }
    else{
        mobile_error.innerHTML="";
    }

    let atPos=email.indexOf("@");
    let dotPos=email.lastIndexOf(".");
    if(email == ""){
        email_error.innerHTML="Email is required";
        error=true;
    }
    else if(atPos<4 ||dotPos-atPos <4 || dotPos > email.length-3){
        email_error.innerHTML="Please enter a valid email";
        error=true;
    }
    else{
        email_error.innerHTML="";
    }

    if(error){
        e.preventDefault();
    }

}