var slider = document.getElementById("busyRange");
var display = document.getElementById("valDisplay");
display.innerHTML = slider.value;

// Update the slider each call
slider.oninput = function() {
    display.innerHTML = this.value;
}