// Team Catbread: Leia Park & Kiran Vuksanaj
// SoftDev pd 9
// K14: Ask Circles [Change || Die] While Moving, etc.
// 2020-03-31

var pic = document.getElementById("vimage");
var id = 0;

var draw = function(e) {
    if (e.target == pic) {
		var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
		var x = e.offsetX; // x coordinate of click
		var y = e.offsetY; // y coordinate of click
		c.setAttribute("cx", x);
		c.setAttribute("cy", y);
		c.setAttribute("r", "10");
		c.setAttribute("fill", "yellow");
		c.setAttribute("stroke", "black");
		c.setAttribute("vx", 3); 
		c.setAttribute("vy", 3);
		pic.appendChild(c); 
    }
}

var movesvg = function(e) {
    circles = pic.children;  
    for (i = 0; i < circles.length; i++) { 
		var circle = circles[i]
		var cx = parseInt(circle.getAttribute("cx")); 
		var cy = parseInt(circle.getAttribute("cy"));
		var vx = parseInt(circle.getAttribute("vx"));
		var vy = parseInt(circle.getAttribute("vy"));
		if (cx >= 490) {  
		    circle.setAttribute("vx",-3);
		}
		else if (cx <= 10) { 
		    circle.setAttribute("vx",3);
		}
		if(cy >= 490) { 
		    circle.setAttribute("vy",-3);
		}
		else if (cy <= 10){ 
		    circle.setAttribute("vy",3);
		}	
		circle.setAttribute("cx",cx + vx);
		circle.setAttribute("cy",cy + vy);
	}
	if (id != 0) {
		id = window.requestAnimationFrame(movesvg);
    }
}

var move = function(e) {
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(movesvg);
}

var clearsvg = function(e) {
    while (pic.lastChild) { 
      pic.removeChild(pic.lastChild); 
    }
    window.cancelAnimationFrame(id);
    id = 0;
}

var getRandomColor = function(e) {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

var xtrasvg = function(e) {
    circles = pic.children;  
    for (i = 0; i < circles.length; i++) {
    	var c = circle[i];
    	c.setAttribute("fill", getRandomColor);
    }
}

var xtra = function(e) {
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(xtrasvg);
}

var clearbutton = document.getElementById("clear");
clearbutton.addEventListener('click', clearsvg);

var movebutton = document.getElementById("move");
movebutton.addEventListener('click', move);

var xtrabutton = document.getElementById("xtra");
xtrabutton.addEventListener('click', xtra);

pic.addEventListener('click', draw);