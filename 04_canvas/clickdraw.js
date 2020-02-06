// state variable: either dot or box
var mode = "dot"

// canvas
var c = document.getElementById("slate")
var ctx = c.getContext("2d")

// clear canvas
function clear() {
     ctx.clearRect(0, 0, 300, 300);
}

// sets mode to dot
function dotmode() {
     mode = "dot"
}

// sets mode to box
function boxmode() {
     mode = "box"
}

// drawing function, takes in mode and cursor location
function draw(e) {
     console.log(e)
     if(mode==="dot"){
          var circle = new Path2D();
          circle.moveTo(e.offsetX, e.offsetY);
          circle.arc(e.offsetX, e.offsetY, 2, 0, 2 * Math.PI);
          ctx.fill(circle);
          console.log("dot")
     }
     else {
          var box = new Path2D();
          box.moveTo(e.offsetX, e.offsetY);
          box.rect(e.offsetX, e.offsetY, 20, 20);
          ctx.fill(box);
          console.log("box")
     }
}

var clearbutton = document.getElementById("clear")
clearbutton.addEventListener('click',clear);

var dotbutton = document.getElementById("dot")
dotbutton.addEventListener('click', dotmode);

var boxbutton = document.getElementById("box")
boxbutton.addEventListener('click', boxmode);

c.addEventListener('click', draw)