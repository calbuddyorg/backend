def handler(event, context):
    # Extract email from the event
    email = event['request']['userAttributes'].get('email')

    if email and 'smsu.edu' in email:
        # Only allow emails from smsu.edu
        event['response']['autoConfirmUser'] = True
        return event
    else:
        # Deny the sign-up
        raise Exception("Only smsu.edu email addresses are allowed to sign up.")
                