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
  if (myIndex==1){
    document.getElementById("quote").style.color="#50577A";
  }
  if (myIndex==2){
    document.getElementById("quote").style.color="white";
  }
  if (myIndex==3){
    document.getElementById("quote").style.color="white";
  } 

  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 4000); // Change image every 4 seconds
}