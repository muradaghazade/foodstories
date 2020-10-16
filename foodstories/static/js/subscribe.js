let url = 'http://127.0.0.1:8000/api/v1/subscribe/';

let form = document.querySelector('.subscribe-form');

form.addEventListener('submit', function(event){
    event.preventDefault();
    let email = document.getElementById('email').value;
    let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let data = {
        'email': email,
    }

    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
      .then(data => {
          console.log(data);
        if (data.email == email) {
            document.querySelector('#message p').innerText = 'You successfully subscribed!';
        }
        else{
            document.querySelector('#message p').innerText = data.email;
        }
    })
})