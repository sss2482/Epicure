var increment=document.getElementsByClassName('plus');
var decrement=document.getElementsByClassName('minus');

console.log(document.getElementById('20'));

for (var i=0;i<increment.length;i++){
     var button=increment[i];
    //  console.log(button);
     button.addEventListener('click',function(event){
        var clicked = event.target;
        // console.log(clicked);
        var out = clicked.parentElement.children[1];

        // console.log();
        var inputValue =out.value;
        // console.log(inputValue);
        var newd = parseInt(inputValue)+1;
        if (newd>15){

            newd=15;
        }
        out.value=newd;

     })
}
for (var i=0;i<decrement.length;i++){
    var button=decrement[i];
   //  console.log(button);
    button.addEventListener('click',function(event){
       var clicked = event.target;
       // console.log(clicked);
       var out = clicked.parentElement.children[1];

       // console.log();
       var inputValue =out.value;
    //    console.log(inputValue);
       var newd = parseInt(inputValue)-1;
       if (newd<0){
        newd=0;
       }
       out.value=newd;

    })
}

function change(){
    document.getElementById('changeform').submit();

}

var a=2;
var sum=0;
function orderit(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    var prices=document.getElementsByClassName('rate');
    // console.log(prices);
    const rates=[];
    for (var i=0;i<prices.length;i++){
        rates.push(parseInt(prices[i].innerHTML))
    }
    var count=document.getElementsByClassName('val');
    const counts=[];
    for (var i=0;i<count.length;i++){
        counts.push(parseInt(count[i].value))
    }
    for (var i=0;i<rates.length;i++){
        sum+=rates[i]*counts[i];
    }
    
    document.getElementById('container3').style.visibility = "visible"; 
    for(var i=0;i<20;i++) {
        var mul = a*30;
        if(counts[i]>0) {
            var mul = a*30;
            console.log(mul);
            document.getElementById(i+20).style.visibility = "visible" ;
            document.getElementById(i+40).innerHTML = counts[i];
            var el = document.getElementById(i+20); 
            el.style.visibility = 'visible';
            el.style.position = 'absolute';
            el.style.top = mul + 'px';
            a++;
        }
    }
    mul++;
    console.log(rates);
    console.log(counts);
    console.log(sum);
    var el = document.getElementById(100);
    console.log(document.getElementById(100));
    el.style.visibility = 'visible';
    el.style.position = 'absolute';
    el.style.top = mul + 'px';
    document.getElementById(101).innerHTML = sum;
    var xox = document.getElementsByClassName('container');
    xox.style.visibility = "hidden";
    // xox.style.pointer-events = 'none';
}