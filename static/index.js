let update_form=document.getElementById("myform")
let btn=document.getElementById("update")
let sf=document.getElementById("StartingPoint")
let d=document.getElementById("Destynation")
let uid=document.getElementById("uid")
btn.addEventListener("click",()=>{
      update_form.style.display="inline"
})
let sub=document.getElementById("submit")
sub.addEventListener("click",update_info)
function update_info()
{   
    let new_sf=sf.value
    let new_d=d.value
    update_form.action=`update/${uid.value}/?q=${new_sf} ${new_d}`
    console.log(update_form.action)
     
}