App.chat = App.cable.subscriptions.create "ChatChannel",
  connected: ->
    console.log("Websocket client connected!")

  disconnected: ->
    # Called when the subscription has been terminated by the server

  received: (data) ->
    console.log(data['message'])

  send_msg: (data) ->
    @perform 'send_msg', message:data
