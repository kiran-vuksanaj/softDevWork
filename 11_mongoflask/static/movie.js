console.log("yo")


let radio_choices = document.getElementsByClassName('form-check');
let currentchoice = "";
let querytext = document.getElementById('querytext');
let queryyear = document.getElementById('queryyear');
console.log(querytext)

console.log(radio_choices);

const enter_yearmode = function(){
    console.log('entering year mode');
    querytext.setAttribute('style','display: none;');
    queryyear.setAttribute('style','display: block;');
}
const enter_normalmode = function(){
    console.log('entering normal mode');
    querytext.setAttribute('style','display: block');
    queryyear.setAttribute('style','display: none');
}

const update_currentchoice = function(e){
    console.log(this.id);
    currentchoice = this.id;
    if(currentchoice==="year_option"){
	enter_yearmode();
    }else{
	enter_normalmode();
    }
}

console.log('adding event listeners')
for(let i = 0; i < radio_choices.length; i++){
    radio_choices[i].addEventListener('click',update_currentchoice);
}
