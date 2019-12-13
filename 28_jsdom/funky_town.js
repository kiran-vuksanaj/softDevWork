// Amanda Chen & Kiran Vuksanaj
// SoftDev1 pd1
// K28 -- Sequential Progression II: Electric Boogaloo
// 2019-12-11

var fact = function(n){
    return (n<=1) ? 1 : n*fact(n-1);
};

// console.log(fact(12));

var fib = function(n){
    if(n == 0) return 0;
    if(n <= 2) return 1;
    return fib(n-2)+fib(n-1);
};

// console.log(fib(8));

var gcd = function(a,b){
    if(a % b == 0){
      return b;
    }
    return gcd(b, a % b);
};

// console.log(gcd(16,8));

var students = ["Roberto","Zachary","Brian","Andrew","Christoper","Steve","Jocelyn","Anabel","Hannah","Louie"]
var randomStudent = function(){
    var i = Math.round(Math.random()*(students.length-1));
    // console.log(i);
    return students[i];
};
//
// console.log(randomStudent());
//
// var yeetdiv = document.getElementById('b')
// var thing = function(){console.log('blue')}
// yeetdiv.addEventListener('click',thing)

var body = document.getElementById("body");
var new_text = document.createElement("p");
body.appendChild(new_text);

var print_fact = function(n){
    var num = fact(5);
    console.log(num);
    new_text.innerHTML = num;
};

var print_fib = function(n){
    var num = fib(7);
    console.log(num);
    new_text.innerHTML = num;
};

var print_gcd = function(n){
    var num = gcd(225,50);
    console.log(num);
    new_text.innerHTML = num;
};

var print_rand_student = function(n){
    var student = randomStudent();
    console.log(student);
    new_text.innerHTML = student;
};

var factButton = document.getElementById('fact-button');
var fibButton = document.getElementById('fib-button');
var gcdButton = document.getElementById('gcd-button');
var randStudentButton = document.getElementById('randstudent-button');

factButton.addEventListener('click',print_fact);
fibButton.addEventListener('click',print_fib);
gcdButton.addEventListener('click',print_gcd);
randStudentButton.addEventListener('click',print_rand_student);
