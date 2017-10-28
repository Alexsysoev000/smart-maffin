function mah (id) {
var x = document.getElementById(id);
if (x.parentNode == this) {
    this.className = "";
    return;
}
x.parentNode.removeChild(x);
this.appendChild(x);
this.className = "";
}