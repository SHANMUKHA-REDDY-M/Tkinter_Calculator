let buttons=document.querySelectorAll("button");
let k=document.getElementById("value");

buttons.forEach(btn=>{
    btn.addEventListener("click",()=>{
        let text=btn.innerText;
        if(text=="C"){
            k.value="";
        }
        else if(text=="DEL"){
            k.value=k.value.slice(0,-1);
        }
        else if(text=="="){
            try{
                k.value=eval(k.value);
            }
            catch{
                k.value="ERROR";
            }
            
        }
        else{
                k.value+=text;
            }
    })
})