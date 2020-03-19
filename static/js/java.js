/*const jumbo = document.querySelector(".jumbotron");
const nadpis = document.querySelector(".nadpis"); 

const tl = new TimelineMax();
tl.fromTo(".container",1,{height:"0%"},{height:"80%", ease: Power2.easeInOut })/*.fromTo(nadpis,1,{opacity:"0"},{opacity:"1", ease: Power2.easeInOut });*/     

gsap.fromTo(".jumbotron", {opacity:"0.1"}, {opacity:"1", duration: 1, ease: Power2.easeInOut});
gsap.fromTo(".container", {x: "-100%", opacity:"0"}, {x: "0%", opacity:"1", duration: 1.5, ease: Power2.easeInOut});
gsap.fromTo(".odtah", {opacity:"0"}, {opacity:"1", duration: 1.2, ease: Power2.easeInOut});



$(document).ready(function(){
  $(".js").hover(function(){
   gsap.fromTo($(this), {y: "0"}, {y: "4", duration: 0.1});
    }, function(){
    gsap.fromTo($(this), {y: "4"}, {y: "0", duration: 0.1});
  });
  
  

  
  
});  





