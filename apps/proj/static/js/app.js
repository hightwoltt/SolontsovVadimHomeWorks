let users = document.querySelectorAll('.user__info')

let clearText
users.forEach(user => {
    let role = user.querySelector('#role')
    if(role.innerHTML == "Admin"){
        user.classList.add('user__gold__border')
    }
    
    user.addEventListener('mouseover', (e) => {
        user.classList.add('event')
        clearTimeout(clearText)
        
        let oldUserInfo = user.innerHTML
        user.querySelector('h1').innerHTML = user.querySelector('#user_name').innerHTML
        user.querySelector('#user_name').outerHTML = ''
        user.addEventListener('mouseout', (e) => {
            user.classList.remove('event')
            clearText = setTimeout(() => {
                user.innerHTML = oldUserInfo
            }, 400);
        })
    })
});
