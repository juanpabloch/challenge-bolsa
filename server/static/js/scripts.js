            
const url = `ws://${window.location.host}/ws/socket-server/api/`
const messages = document.querySelector('#product_info')

const webSocket = new WebSocket(url)

webSocket.onopen = function(e){
    webSocket.send(JSON.stringify({
        "message": code,
    }))
}

webSocket.onmessage = function(e){
    let data = JSON.parse(e.data)
    messages.innerHTML = ''
    messages.insertAdjacentHTML('beforeend',
        `<h3 class="mt-5 mb-5">Cargando datos...<h3/>`
    )
    console.log('Data: ', data)

    if(data.type === 'product'){
        messages.innerHTML = ''
        messages.insertAdjacentHTML('beforeend', `
        <div class="card mb-5" id="card_info">
            <h5 class="card-header">${data.message.code}</h5>
            <div class="card-body text-center">
            <p class="card-text mb-4">${data.message.description}</p>
            <div class="card_price">
                    <div>
                        <p class="mb-0">Venta</p>
                        <h4>$${data.message.sell}</h4>
                    </div>
                    <div>
                        <p class="mb-0">Compra</p>
                        <h4>$${data.message.buy}</h4>
                    </div>
            </div>
            </div>
        </div>
        `)
    }
}

webSocket.onclose = function(e){
    console.info('webSocket close')
}

setInterval(() => {
    webSocket.send(JSON.stringify({
        "message": code,
    }))
    }, 60000);
