function passwordVisibility() {
    var element = document.getElementById('pass-input');
    var x = document.getElementById('icon-1');
    if(element.type === 'password') {
        element.type = 'text';
    }else {
        element.type = 'password';
    }
}