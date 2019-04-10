const divBot = document.querySelector("#bot");
const inputMessage = document.querySelector("#input-message");
const urlA = 'http://localhost:5005/webhooks/rest/webhook';
const urlI = 'http://localhost:5006/webhooks/rest/webhook';
const urlC = 'http://localhost:5007/webhooks/rest/webhook';
const urlR = 'http://localhost:5008/webhooks/rest/webhook';


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
            "sender" : "Bots",
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

        fetch(urlA, fetchData)
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
	fetch(urlI, fetchData)
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
	fetch(urlC, fetchData)
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
	fetch(urlR, fetchData)
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



