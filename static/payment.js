const data= document.currentScript.dataset;
const orderTotal= parseInt(data.orderTotal);
console.log(orderTotal)
document.getElementsByClassName("total-price")[0].innerHTML=`Total Price: ${orderTotal}`;
var orderedItems = JSON.parse(document.getElementById('orderedItems').textContent);

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
document.getElementsByClassName("qr-image")[0].src=`https://api.qrserver.com/v1/create-qr-code/?data=upi%3A%2F%2Fpay%3Fpa%3D7901040555%40paytm%26pn%3DEpicure%26tn%3DTest%2520Payment%26am%3D${orderTotal}%26cu%3DINR%3E%26tr%3D%3C1%3Esize=200x200`
// Add a click event listener to the "Pay Now" button
document.getElementById("pay-now-btn").addEventListener("click", function() {
    // Get the payment details from the QR code
    var paymentDetails = {  pa: "7901040556@paytm", pn: "Epicure",tn: "Test%20Payment",am: "1.00",cu: "INR",tr: "1"}
    // console.log(paymentDetails)
    // Call the payment gateway API to process the payment
    callPaymentGatewayAPI(paymentDetails, function(response) {
      // Handle the payment response
      if (response.status === "success") {
        // Update the payment status on your website
        updatePaymentStatus(response.paymentId, "paid");
        
        // Display a success message to the user
        displaySuccessMessage();
      } else {
        // Display an error message to the user
        displayErrorMessage();
      }
    });
  });
  
  // Function to get the payment details from the QR code
  function getPaymentDetails() {
    // Parse the QR code data to extract the payment details
    var qrCodeData = encoded_data;
    console.log(qrCodeData)
    qrCodeData=decodeURIComponent(qrCodeData);
    var paymentDetails = qrCodeData.split(":")[1].split("&");
    console.log(paymentDetails)
    var paymentData = {};
  
    for (var i = 0; i < paymentDetails.length; i++) {
      var keyValuePair = paymentDetails[i].split("=");

      paymentData[keyValuePair[0]] = keyValuePair[1];
    }
  
    return paymentData;
  }
  
  // Function to call the payment gateway API to process the payment
  function callPaymentGatewayAPI(paymentDetails, callback) {
    // Make an AJAX call to the payment gateway API with the payment details
    // and handle the response using the callback function
    // This code will depend on the payment gateway and API you are using
    // Consult their documentation for the specific implementation details
    // Here is an example code using jQuery:
    
    $.ajax({
      url: "https://api.phonepe.com/v4/payment",
      type: "POST",
      data: paymentDetails,
      success: function(response) {
        callback(response);
      },
      error: function(xhr, status, error) {
        console.log("Error processing payment:", error);
        callback({ status: "error" });
      }
    });
  }
  
  // Function to update the payment status on your website
  function updatePaymentStatus(paymentId, status) {
    // Make an AJAX call to your server with the payment ID and status
    // This code will depend on your server-side implementation
    // Here is an example code using jQuery:
  
    $.ajax({
      url: "/update-payment-status",
      type: "POST",
      data: {
        paymentId: paymentId,
        status: status
      },    
      
      success: function(response) {
        console.log("Payment status updated successfully:", response);
      },
      error: function(xhr, status, error) {
        console.log("Error updating payment status:", error);
      }
    });
  }
  
  // Function to display a success message to the user
  function displaySuccessMessage() {
    // Display a success message to the user on your website's payment page
    // This code will depend on your website's implementation
    alert('Payment was successful!');
  }
  
  // Function to display an error message to the user
  function displayErrorMessage() {
    // Display an error message to the user on your website's payment page
    // This code will depend on your website's implementation
    alert('Payment failed. Please try again later.');
  }
  