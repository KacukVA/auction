const lot_id = window.location.pathname.split('/')[2];
let ws = new WebSocket(`ws://127.0.0.1:8000/ws/lot/${lot_id}/`)

$('.update').click(function () {
    const new_price = $('input').val();
    ws.send(new_price)
})

ws.onmessage = function (data) {
    $('.current-price').text(data.data)
}
