const data= document.currentScript.dataset;
const orderTotal = data.totalCost;
console.log('hello');
console.log(orderTotal);
var orders={};
var i=0;

document.getElementById("total-price").innerHTML=`Total Price: ${orderTotal}`;
console.log(data.orderDetails)
var orderedItems = JSON.parse(data.orderDetails);
console.log(orderedItems);
// Loop through the ordered items and display them
var orderedItemsList = document.getElementById('ordered-items');
for (var i = 0; i < orderedItems.length; i++) {
        var item = orderedItems[i];
        var itemName = item.name;
        var itemPrice = item.price;
        var itemQuantity = item.quantity;
  
        var listItem = document.createElement('li');
        listItem.innerHTML = `${itemName} - ${itemQuantity} x ${itemPrice} = ${itemQuantity * itemPrice}`;
  
        orderedItemsList.appendChild(listItem);
}
price={total: orderTotal}
console.log(price)
orderedItems.push(price)
console.log(orderedItems)
document.getElementsByClassName("qr-image")[0].src=`https://api.qrserver.com/v1/create-qr-code/?data=upi%3A%2F%2Fpay%3Fpa%3D7842559379%40paytm%26pn%3DEpicure%26tn%3DTest%2520Payment%26am%3D${orderTotal}%26cu%3DINR%3E%26tr%3D%3C1%3Esize=200x200`;
function store(){
        if(localStorage.hasOwnProperty('orde')){
                orders=JSON.parse(localStorage.getItem('orde'))
        }
        console.log(1)
        i=Object.keys(orders).length +1
        console.log(1)
        orders[i]=orderedItems
        console.log(1)
        localStorage.setItem('orde', JSON.stringify(orders))
        console.log(1)
        window.location.href='orders.html'
}
function cancel(){
        window.location.href='Menu.html';
}

function done(){
        console.log('hello')
        document.getElementById('id_transaction_id').setAttribute('required','');
        address_element=document.getElementById('id_address');
        address_element.setAttribute('required','');
        address=address_element.value;
        document.getElementById('input_address').value=address;
        document.getElementById("form").submit();
        
}