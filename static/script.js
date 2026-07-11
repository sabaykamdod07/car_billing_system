document.addEventListener("DOMContentLoaded",()=>{

const discount=document.querySelector("input[name='discount']");

const button=document.querySelector("button");

discount.addEventListener("input",()=>{

if(discount.value.endsWith("%")){

discount.style.color="green";

}
else{

discount.style.color="#2563eb";

}

});

button.addEventListener("mouseenter",()=>{

button.style.boxShadow="0 10px 25px rgba(37,99,235,.4)";

});

button.addEventListener("mouseleave",()=>{

button.style.boxShadow="none";

});

});