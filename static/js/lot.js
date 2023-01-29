const lot_id = window.location.pathname.split('/')[2];
let ws = new WebSocket(`ws://127.0.0.1:8000/ws/lot/${lot_id}/`)
