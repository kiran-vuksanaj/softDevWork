// Leia Park & Alice Ni
// SoftDev pd 9
// K13 : Ask Circles [Change || Die]
// 2020 03 30



var pic = document.getElementById("vimage");

var draw = function(e) {
    if (e.target == pic){ //if event is on empty space
	var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	var x = e.offsetX; // x coordinate of click
	var y = e.offsetY; // y coordinate of click
	c.setAttribute("cx", x);
	c.setAttribute("cy", y);
	c.setAttribute("r", "10");
	c.setAttribute("fill", "yellow");
	c.setAttribute("stroke", "black");
	pic.appendChild(c); // adds circle to svg picture
    }
    else if (e.target.getAttribute("fill") == "yellow"){ // if event is on a yellow circle
	e.target.setAttribute("fill", "red"); //change color to red
    }
    else{
	pic.removeChild(e.target); // removes red circle
	var x = Math.random() * 500 //generate random x coordinate
	var y = Math.random() * 500 //generate random y coordinate
	var k = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	k.setAttribute("cx", x);
	k.setAttribute("cy", y);
	k.setAttribute("r", "10");
	k.setAttribute("fill", "yellow");
	k.setAttribute("stroke", "black");
	pic.appendChild(k); // adds circle to svg picture
    }
}

var clearsvg = function(e) {
  while (pic.lastChild) { // while there are still shapes
    pic.removeChild(pic.lastChild); //remove the previously drawn shape
  }
}

var clearbutton = document.getElementById("clear");
clearbutton.addEventListener('click', clearsvg);
pic.addEventListener('click', draw);
