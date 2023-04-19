


var myIndex = 0;
carousel();
function carousel() {
  var i;
  var x = document.getElementsByClassName("imh");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 3000); // Change image every 2 seconds
}

var myIndex1 = 0;


function carousel1() {
  var i;
  var x = document.getElementsByClassName("imh1");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex1++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel1, 3000); // Change image every 2 seconds
}

function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function changeclass() {
  var element = document.getElementById('profile-box');
  element.classList.toggle('new-profile-box');
  var element_1 = document.getElementById('container-2');
  element_1.classList.toggle('new-main-container');
}


