

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


