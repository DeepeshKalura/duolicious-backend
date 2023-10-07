def big_part(has_intro, has_chat):
    if has_intro and has_chat:
        return 'You have new messages in your chats and intros!'
    if has_intro:
        return 'You have a new message in your intros!'
    if has_chat:
        return 'You have a new message in your chats!'
    return (
        "Our email notifier is broken 😵‍💫. Please report this "
        "to support@duolicious.app")

def little_part(has_intro, has_chat):
    if has_intro and has_chat:
        return 'Open the app to read them'
    return 'Open the app to read it'

def emailtemplate(has_intro, has_chat):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>You Have a New Message!</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif;">
        <table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
            <tr>
                <td align="center">
                    <table width="600" cellspacing="0" cellpadding="0" border="0" align="center">
                        <tr>
                            <td bgcolor="#70f" align="center">
                                <img src="https://email-assets.duolicious.app/header-logo.png" alt="Duolicious Logo" width="108" height="50" />
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#f1e5ff" height="20">&nbsp;</td>
                        </tr>
                        <tr>
                            <td bgcolor="#f1e5ff" align="center" style="color: #70f;">
                                <p style="color: #70f; font-size: 20px; font-weight: 900;">{big_part(has_intro, has_chat)}</p>
                                <p style="color: #70f; font-size: 16px">{little_part(has_intro, has_chat)}</p>
                            </td>
                        </tr>
                        <tr>
                            <td bgcolor="#f1e5ff" height="20">&nbsp;</td>
                        </tr>
                        <tr>
                            <td bgcolor="#70f" height="50">&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """