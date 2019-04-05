const divBot = document.querySelector("#bot");
const inputMessage = document.querySelector("#input-message");
const url = 'http://localhost:5005/webhooks/rest/webhook';


if(divBot == null) {
    throw "Problem with the div";
}

inputMessage.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        let textInput = inputMessage.value;
        inputMessage.value = "";
        const p = document.createElement("p");
        p.innerText = textInput;
        p.style = "color : blue";
        divBot.append(p);

        let data = {
            "sender" : "Etienne",
            "message" : textInput
        };


        let fetchData = {
            method: 'POST',
            body: JSON.stringify(data),
            headers:  new Headers({
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        })
        };

        fetch(url, fetchData)
            .then((data) => {
                data.json().then((json) => {
                    const p2 = document.createElement("p");
                    p2.innerText = json[0].text;
                    p2.style = "color : red";
                    divBot.append(p2);
                });
            })
            .catch( (error) => {
                console.error(error);
        });

    }
});



