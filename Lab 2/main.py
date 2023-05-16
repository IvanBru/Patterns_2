from mediator import OrderPageMediator

mediator = OrderPageMediator()
selected_date = "2023-01-03"
mediator.handle_date_selection(selected_date)
mediator.handle_recipient_checkbox(True)
mediator.handle_pickup_option(True)