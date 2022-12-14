let some = document.getElementById('user-name')
if(some.innerHTML == 'AnonymousUser'){
    some.innerHTML = 'Login'
}
else{
    some.pathname = '/profile/'
}



let buttons= Array.from(document.getElementsByClassName('about-quantity'))
buttons.forEach(element =>{
    element.addEventListener('click',()=>{
        id = element.getAttribute('id')
        value = element.getAttribute('value')
        addtocart(id, value)
        
    })
})

function addtocart(id , value)
{
    data = {'value':value}
    fetch(
        url=`/add_to_cart/${id}/`,{
            method : 'POST',
            headers : {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body : JSON.stringify(data)
        }  
        )
        .then(res => {
            res.json,
            location.reload()
        })
        .then(res => {
            console.log(res.data)

        })
        .catch(err => console.log(err))
        
}


